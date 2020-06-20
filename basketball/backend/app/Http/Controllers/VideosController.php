<?php

namespace App\Http\Controllers;

use FFMpeg;
use Illuminate\Http\Request;
use App\Models\ActionFrame;
use App\Models\ActionResult;
use App\Models\Skeleton;
use App\Models\ActionCategory;

class VideosController extends Controller
{
    /**
     * 新增视频
     */
    public function videoadd(Request $request)
    {
        //获取post提交的数据
        $data=$_POST;
        $file=$request->file('file');
        $clientName=$_FILES['file']['name'];
        $extension=explode('.',$clientName);
        $file_size=$_FILES['file']['size'];
        $tmpName=$_FILES['file']['tmp_name'];
        $type=$_FILES['file']['type'];
        $newName = md5(date('ymdhis').$clientName).".".$extension[1];
        //$file->move(app_path().'/storage/uploads',$newName);
        $file->move('storage',$newName);
        return response()->json([
            'status' => 'success',
            'status_code' => 200,
            'data' => $newName,
            'user'=>$newName
        ]);
    }
    /**
     *  切分视频
     */
    public function videocut(){
        $allda=$_GET['info'];//上传文件的数组，包括视频名称，视频类型，动作类型，是否标准动作
        $da=explode('-',$allda[0]);//切分接收到的数据
        $filearray=$da[0];
        $action_type=$da[1];
        $video_type=$da[2];
        $is_standard=$da[3];
        $actioncategorys = ActionCategory::find($action_type);//查找动作名称
        $ceo = ["投篮"=>"shoot","运球"=>"dribble","传球"=>"pass"];//构建键值对数组
        $video_path=storage_path().'/app/public/'.$filearray;
        if($is_standard=='1'){//上传视频为标准动作
            $res=$this->standard($video_type,$video_path,$ceo,$da,$actioncategorys);
        }else{//is_standard=0为测试动作
            $res=$this->test($video_type,$video_path,$ceo,$da,$actioncategorys);
        }
        return $res;
    }
    /**
     * 上传标准动作视频处理方法
    */
    public function standard($video_type,$video_path,$ceo,$da,$actioncategorys){
        
        if($video_type=='1'){//如果上传的是彩色视频
            $picture_path=storage_path().'/app/public/standard_action/color_action/'.$ceo[$actioncategorys->name].'/';//彩色图像的地址    
        }else{//如果上传的是深度视频
            $picture_path=storage_path().'/app/public/standard_action/depth_action/'.$ceo[$actioncategorys->name].'/';//深度图像的地址
        }
        if(is_dir($picture_path)){//判断目录是否存在
            
        }else{
            mkdir($picture_path,0777,true);//
        }
        $p_path=$picture_path;
        $str = "ffmpeg -i ".$video_path." ".$p_path.$ceo[$actioncategorys->name]."_%05d.png";
        system($str);
        $mark=0;
        if($video_type=='1'){//如果是彩色视频，判断深度图片是否已上传
            $t_path=storage_path().'/app/public/standard_action/depth_action/'.$ceo[$actioncategorys->name].'/';
        }else{
            $t_path=storage_path().'/app/public/standard_action/color_action/'.$ceo[$actioncategorys->name].'/';
        }
        if(is_dir($t_path)){//判断对应目录是否存在
            $dir=scandir($t_path);
            if (!empty($dir[2])) {//判断彩色图和深度图是否都存在，是的话则不刷新页面，进行分析
                $mark=1;
            }
        }
        return response()->json([
            'status' => 'success',
            'status_code' => 200,
            'mark'=>$mark,
            'allda'=>$da,//传递视频信息
            'data' => $p_path,
            'actiontype'=>$ceo[$actioncategorys->name]
        ]);
    }
    /**
     * 上传测试动作视频处理方法
    */
    public function test($video_type,$video_path,$ceo,$da,$actioncategorys){
        $user = auth('api')->user();//获取运动员的id，创建对应文件夹
        $a_path=storage_path().'/app/public/test_action/athlete-'.$user->id.'/';
        if($video_type=='1'){//如果上传的是彩色视频
            $picture_path=$a_path.$ceo[$actioncategorys->name].'/color_action/';//彩色图像的地址    
        }else{//如果上传的是深度视频
            $picture_path=$a_path.$ceo[$actioncategorys->name].'/depth_action/';//深度图像的地址
        }
        if(is_dir($picture_path)){//判断目录是否存在
            
        }else{
            mkdir($picture_path,0777,true);//
        }
        $p_path=$picture_path;
        $str = "ffmpeg -i ".$video_path." ".$p_path.$ceo[$actioncategorys->name]."_%05d.png";
        system($str);
        $mark=0;
        if($video_type=='1'){//如果是彩色视频，判断深度图片是否已上传
            $t_path=$a_path.$ceo[$actioncategorys->name].'/depth_action/';
        }else{
            $t_path=$a_path.$ceo[$actioncategorys->name].'/color_action/';
        }
        if(is_dir($t_path)){//判断对应目录是否存在
            $dir=scandir($t_path);
            if (!empty($dir[2])) {//判断彩色图和深度图是否都存在，是的话则不刷新页面，进行分析
                $mark=1;
            }
        }
        return response()->json([
            'status' => 'success',
            'status_code' => 200,
            'mark'=>$mark,
            'allda'=>$da,//传递视频信息
            'data' => $p_path,
            'userid'=>$user->id,
            'actiontype'=>$ceo[$actioncategorys->name]
        ]);
    }
    /**
     * 获取视频分析的结果图片
    */
    public function videoresult(){
        $beforepath=$_GET['info'];//获取切分图片的路径
        $path=storage_path().'/app/public/'.$beforepath.'/';//获取结果路径
        if(is_dir($path)){//判断对应结果目录是否存在
            
        }else{
            mkdir($path,0777,true);//创建对应文件夹
        }
        $files=[];//文件数组
        $filesname=[];//只有文件名称
        $dir = new \DirectoryIterator($path);
        foreach ($dir as $key => $file){
            if($file->getFilename() == '.' || $file->getFilename() == '..'){
                continue;
            }
            $files[] = $file->getPathname();
            if($file->isDir()){
                $files = array_merge($files, $this->ergodicDir5($file->getPathname()));
            }
        }
        //对files进行处理，获得只有文件名的数组
        foreach($files as $key=>$f){
            $arr=explode('/',$f);//获取文件名
            array_push($filesname,$arr[count($arr)-1]);
            if($arr[count($arr)-1]=='frames_00001.png'){
                break;
            }
        }
        return response()->json([
            'status' => 'success',
            'status_code' => 200,
            'data' => $filesname
        ]);
    }
    /**
     * 获取测试动作的分析结果
    */
    public function videoposeresult(){
        $frame=$_GET;//获取测试动作id和frame_id
        $actionframe=ActionFrame::where('action_id',$frame['action_id'])->where('is_standard','0')->first();//获取动作视频帧
        $skeleton=Skeleton::where('action_frame_id', $actionframe->id)->where('frame',$frame['frame'])->first();
        $actionresult=ActionResult::where('skeleton_id',$skeleton->id)->first();
        return response()->json([
            'status' => 'success',
            'status_code' => 200,
            'data' => $actionresult,
        ]);
    }
     /**
     * 添加测试动作的分析结果
    */
    public function videoaddresult(Request $request){
        $frame=$_POST;//获取测试动作id和frame_id,result
        $actionframe=ActionFrame::where('action_id',$frame['action_id'])->where('is_standard','0')->first();//获取动作视频帧
        $skeleton=Skeleton::where('action_frame_id', $actionframe->id)->where('frame',$frame['frame'])->first();
        $actionresult = new ActionResult();
        $actionresult->skeleton_id=$skeleton->id;
        $actionresult->result=$frame['result'];
        $actionresult->save();
        return response()->json([
            'status' => 'success',
            'status_code' => 200,
            'data' => $actionresult->result,
        ]);
    }
}

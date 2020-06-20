<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\ActionCategory;

class ActionsController extends Controller
{
    /**
     * 获取动作列表
     */
    public function actions()
    {
        $user = auth('api')->user();
        if($user!=""){//判断用户是否有访问接口的权限
            $actioncategorys = ActionCategory::all();
            return response()->json([
                'status' => 'success',
                'status_code' => 200,
                'actions' => $actioncategorys,
                'user' => $user
            ]); 
        }else{
            return \Response::json([
                'status'=>'not found',
                'status_code'=> 404,
            ]);
        }       
    }
    /**
     * 获取动作类别信息
     */
    public function info()
    {
        $user = auth('api')->user();
        $action_code=$_GET["action_code"];
        if($user!=""){//判断用户是否有访问接口的权限
            $actioninfo = ActionCategory::find($action_code);
            return response()->json([
                'status' => 'success',
                'status_code' => 200,
                'actioninfo' => $actioninfo,
                'user' => $user
            ]); 
        }else{
            return \Response::json([
                'status'=>'not found',
                'status_code'=> 404,
            ]);
        }       
    }
    
    /**
     * 新增动作类别
     */
    public function add(Request $request)
    {
        $user = auth('api')->user();
        if($user!=""){//判断用户是否有访问接口的权限
            //获取post提交的数据
            $data=$_POST;
            //Validation（判断用户的数据是否合法）
            $this->validate($request, [
                'name'=>'required',//动作类别名称
            ]);
            $addaction = new ActionCategory();
            $addaction->name = $data['name'];
            $addaction->save();
            
            return response()->json([
                'status' => 'success',
                'status_code' => 200,
                'data' => $data,
                'user' => $user]);
        }else{
            return \Response::json([
                'status'=>'not found',
                'status_code'=> 404,
            ]);
        }
    }
}

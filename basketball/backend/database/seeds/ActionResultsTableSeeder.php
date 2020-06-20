<?php

use Illuminate\Database\Seeder;
use App\Models\ActionResult;
use App\Models\ActionFrame;
use App\Models\Skeleton;

class ActionResultsTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $faker = Faker\Factory::create('zh_CN');
        //动作比对结果表
        ActionResult::truncate();
        $actionresult=new ActionResult();
        $arr=['1','2','3'];//视频帧
        $actionFrame=ActionFrame::where('is_standard','0')->get();//查找测试动作的视频帧
        foreach($actionFrame as $ac){
            for($i=0;$i<count($arr);$i++){
                $skeleton=Skeleton::where('action_frame_id',$ac->id)->where('frame',$arr[$i])->get();//找到测试动作对应的视频帧骨架坐标
                $text=$faker->realText();
                foreach($skeleton as $ske){//循环测试动作骨架坐标
                    $actionresult=new ActionResult();
                    $actionresult->skeleton_id=$ske->id;
                    $actionresult->result=$text;
                    $actionresult->save();
                }
            }
        }
    }
}

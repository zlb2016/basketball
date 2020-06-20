<?php

use Illuminate\Database\Seeder;
use App\Models\ActionFrame;

class ActionFramesTableSeeder extends Seeder
{
   /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        //动作视频帧数据填充
        ActionFrame::truncate();
        //随机生成三种动作id的数据
        for($i=0;$i<6;$i++){
            $actionframe=new ActionFrame();
            if($i>2){
                $actionframe->action_id=$i-2;
            }else{
                $actionframe->action_id=$i+1;
            }
            $actionframe->frames='1,2,3';
            $actionframe->person_id=$i+1;
            if($i%2==0){
                $actionframe->is_standard=1;
            }else{
                $actionframe->is_standard=0;
            }
            //$actionframe->is_standard=rand(0,1);
            $actionframe->save();
        }
    }
}

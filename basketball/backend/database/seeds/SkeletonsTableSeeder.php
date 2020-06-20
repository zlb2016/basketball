<?php

use Illuminate\Database\Seeder;
use App\Models\Skeleton;
use App\Models\ActionFrame;

class SkeletonsTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        $faker = Faker\Factory::create('zh_CN');
        //视频帧骨架
        $actionframe=ActionFrame::all();
        foreach($actionframe as $ac){//循环动作视频帧表
            //for($ac->frames)
            $array=explode(',',$ac->frames); 
            for($i=0;$i<count($array);$i++){
                for($j=0;$j<17;$j++){//17个关键点
                    $skeleton=new Skeleton();
                    $skeleton->action_frame_id=$ac->id;
                    $skeleton->frame=$array[$i];
                    $skeleton->coordinate=$this->coordinate($faker);
                    $skeleton->save();
                }
            }
            
        }  
    }
    private function coordinate($faker){//生成三维坐标
            $x=$faker->randomFloat(2, 0, 10);
            $y=$faker->randomFloat(2, 0, 10);
            $z=$faker->randomFloat(2, 0, 10);
            $coor=($x.','.$y.','.$z);
            return $coor;
    }
}

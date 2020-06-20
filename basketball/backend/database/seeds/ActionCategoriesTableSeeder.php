<?php

use Illuminate\Database\Seeder;
use App\Models\ActionCategory;

class ActionCategoriesTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        //
        ActionCategory::truncate();
        $arr=array('shoot','pass','dribble');//投篮、传球、运球三个动作
        for($i=0;$i<count($arr);$i++){
            $actioncate=new ActionCategory();
            $actioncate->name=$arr[$i];
            $actioncate->save();
        }
    }
}

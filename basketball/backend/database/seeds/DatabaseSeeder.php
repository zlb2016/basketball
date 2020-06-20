<?php

use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        //$this->call(UsersTableSeeder::class);
        //$this->call(ActionCategoriesTableSeeder::class);//动作类别表
        //$this->call(ActionFramesTableSeeder::class);//动作视频帧表
        //$this->call(SkeletonsTableSeeder::class);//视频帧骨架表
        $this->call(ActionResultsTableSeeder::class);//视频结果表
    }
}

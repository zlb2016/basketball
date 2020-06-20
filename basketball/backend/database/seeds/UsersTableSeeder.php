<?php

use Illuminate\Database\Seeder;
use App\Models\User;

class UsersTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        User::truncate();
        $this->leader();
        $this->systemadmin();
        $this->fixperson();
    }
    /**
     * 添加负责人（1名）
     */
    private function leader(){
        $user=new User();
        $user->name='张学兵';
        $user->email='test@163.com';
        $user->password=bcrypt('secret');
        $user->remember_token= str_random(10);
        $user->avatar='public/images/leader.png';
        $user->serialnum='1101';
        $user->duty='超级管理员';
        $user->save();
    }
    /**
     * 添加教练员（2名）
     */
    private function systemadmin(){
        $faker = Faker\Factory::create('zh_CN');
        for($i=0;$i<2;$i++){
            $user=new User();
            $user->name=$faker->name('male');
            $user->email='test'.$i.'@163.com';
            $user->password=bcrypt('secret');
            $user->remember_token= str_random(10);
            $user->avatar='public/images/admin-'.$i.'.png';
            $user->serialnum='111'.$i;
            $user->duty='教练员';
            $user->save();
        }
    }
    /**
     * 添加运动员（5名）
     */
    private function fixperson(){
        $faker = Faker\Factory::create('zh_CN');
        for($i=0;$i<5;$i++){
            $user=new User();
            $user->name=$faker->name('male');
            $user->email='testfix'.$i.'@163.com';
            $user->password=bcrypt('secret');
            $user->remember_token= str_random(10);
            $user->avatar='public/images/fix-'.$i.'.png';
            $user->serialnum='112'.$i;
            $user->duty='运动员';
            $user->save();
        }
    }
}

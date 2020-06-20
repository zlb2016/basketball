<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Http\Requests;
use App\Models\User;
use Auth;

class UsersController extends Controller
{
    /**
     * 获取用户列表
     */
    public function users()
    {
        $user = auth('api')->user();
        if($user!=""){//判断用户是否有访问接口的权限
            $users = User::all();
            return response()->json([
                'status' => 'success',
                'status_code' => 200,
                'users' => $users,
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
     * 获取人员信息
     */
    public function info()
    {
        $user = auth('api')->user();
        $user_code=$_GET["user_code"];
        if($user!=""){//判断用户是否有访问接口的权限
            if($user_code!=0){
                $userinfo = User::where('serialnum',$user_code)->first();
            }else{
                $userinfo=$user;
            }
            return response()->json([
                'status' => 'success',
                'status_code' => 200,
                'userinfo' => $userinfo,
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
     * 新增人员
     */
    public function add(Request $request)
    {
        $user = auth('api')->user();
        if($user!=""){//判断用户是否有访问接口的权限
            //获取post提交的数据
            $data=$_POST;
            //Validation（判断用户的数据是否合法）
            $this->validate($request, [
                'name'=>'required',//人员姓名
                'email'=>'required',//邮箱
                'password'=>'required',//密码
                'avatar'=>'required',//人员照片的url
                'duty'=>'required',//人员职务
                'serialnum'=>'required'//人员编号
            ]);
            $adduser = new User();
            $adduser->name = $data['name'];
            $adduser->email = $data['email'];
            $adduser->password = bcrypt($data['password']);
            $adduser->avatar=$data['avatar'];
            $adduser->duty=$data['duty'];
            $adduser->serialnum = $data['serialnum'];
            $adduser->save();
            
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

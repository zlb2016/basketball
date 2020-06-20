<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

//需要token验证的接口
Route::group(['prefix'=>'v1','middleware'=>'jwt.auth'],function(){
    /*
    | 用户列表接口
    |-------------------------------------------------------------------------------
    */
    Route::prefix('users')->group(function () {
        /*
        |-------------------------------------------------------------------------------
        | 获取人员列表
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/users
        | Controller:     
        | Method:         GET
        | Description:    获取人员列表数据
        */
        Route::get('/','UsersController@users');
        /*
        |-------------------------------------------------------------------------------
        | 获取人员信息
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/users/{id}
        | Controller:     
        | Method:         GET
        | Description:    获取人员信息数据
        */
        Route::get('/{id}','UsersController@info');
        /*
        |-------------------------------------------------------------------------------
        | 添加人员
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/users/add
        | Controller:     
        | Method:         POST
        | Description:    添加人员信息
        */
        Route::post('/add','UsersController@add');
    });
    /*
    | 动作类别接口
    |-------------------------------------------------------------------------------
    */
    Route::prefix('actions')->group(function () {
        /*
        |-------------------------------------------------------------------------------
        | 获取动作类别列表
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/actions
        | Controller:     
        | Method:         GET
        | Description:    获取动作类别列表
        */
        Route::get('/','ActionsController@actions');
        /*
        |-------------------------------------------------------------------------------
        | 获取动作类别信息
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/actions/{id}
        | Controller:     
        | Method:         GET
        | Description:    获取动作类别信息数据
        */
        Route::get('/{id}','ActionsController@info');
        /*
        |-------------------------------------------------------------------------------
        | 添加动作类别
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/actions/add
        | Controller:     
        | Method:         POST
        | Description:    添加人员信息
        */
        Route::post('/add','ActionsController@add');
    });
    /*
        |-------------------------------------------------------------------------------
        | 获取上传的视频
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/videos/add
        | Controller:     
        | Method:         POST
        | Description:    获取上传的视频
        */
        Route::post('videos/add','VideosController@videoadd'); 
    /*
        |-------------------------------------------------------------------------------
        | 进行视频切分
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/videos/cut
        | Controller:     
        | Method:         get
        | Description:    进行视频切分  
    */
        Route::get('videos/cut','VideosController@videocut');
     /*
        |-------------------------------------------------------------------------------
        | 获取视频分析的结果图片
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/videos/results
        | Controller:     
        | Method:         get
        | Description:    获取视频分析的结果图片    
    */
        Route::get('videos/results','VideosController@videoresult');
    /*
        |-------------------------------------------------------------------------------
        | 获取测试动作的姿态分析结果
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/videos/poseresult
        | Controller:     
        | Method:         post
        | Description:    获取测试动作的姿态分析结果，如果没有数据，则进行姿态分析后，将比较结果存储到数据库中
     */
        Route::get('videos/poseresult','VideosController@videoposeresult');
         /*
        |-------------------------------------------------------------------------------
        | 获取第一次姿态识别的分析结果(post方法)
        |-------------------------------------------------------------------------------
        | URL:            /api/v1/videos/addresult
        | Controller:     
        | Method:         post
        | Description:    获取第一次姿态识别的分析结果
     */
        Route::post('videos/addposeresult','VideosController@videoaddresult');
});

Route::group([

    'prefix' => 'auth'

], function ($router) {

    Route::post('login', 'AuthController@login');
    Route::post('logout', 'AuthController@logout');
    Route::post('refresh', 'AuthController@refresh');
    Route::post('me', 'AuthController@me');
});


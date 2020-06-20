<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateActionFramesTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('action_frames', function (Blueprint $table) {
            $table->increments('id');
            $table->string('action_id');//动作类别id
            $table->string('frames');//连续的视频帧
            $table->string('person_id');//人员id
            $table->string('is_standard');//是否标准动作：0:不是,1:是
            $table->softDeletes();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('action_frames');
    }
}

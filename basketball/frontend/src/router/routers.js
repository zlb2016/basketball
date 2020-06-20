import Main from '@/components/main'
/**
 * import parentView from '@/components/parent-view'
*/

/**
 * iview-admin中meta除了原生参数外可配置的参数:
 * meta: {
 *  title: { String|Number|Function }
 *         显示在侧边栏、面包屑和标签栏的文字
 *         使用'{{ 多语言字段 }}'形式结合多语言使用，例子看多语言的路由配置;
 *         可以传入一个回调函数，参数是当前路由对象，例子看动态路由和带参路由
 *  hideInBread: (false) 设为true后此级路由将不会出现在面包屑中，示例看QQ群路由配置
 *  hideInMenu: (false) 设为true后在左侧菜单不会显示该页面选项
 *  notCache: (false) 设为true后页面在切换标签后不会缓存，如果需要缓存，无需设置这个字段，而且需要设置页面组件name属性和路由配置的name一致
 *  access: (null) 可访问该页面的权限数组，当前路由设置的权限会影响子路由
 *  icon: (-) 该页面在左侧菜单、面包屑和标签导航处显示的图标，如果是自定义图标，需要在图标名称前加下划线'_'
 *  beforeCloseName: (-) 设置该字段，则在关闭当前tab页时会去'@/router/before-close.js'里寻找该字段名对应的方法，作为关闭前的钩子函数
 * }
 */

export default [
  {
    path: '/',
    name: 'login',
    meta: {
      title: 'Login - 登录',
      hideInMenu: true
    },
    component: () => import('@/view/login/login.vue')
  },
  {
    path: '/home',
    name: '首页',
    redirect: '/home',
    component: Main,
    meta: {
      hideInMenu: true,
      notCache: true
    },
    children: [
      {
        path: '/home',
        name: '首页',
        meta: {
          hideInMenu: true,
          title: '首页',
          notCache: true,
          icon: 'md-home'
        },
        component: () => import('@/view/single-page/home/home.vue')
      },
      
    ]
  },
  {
    path: '/coach',
    name: '教练员管理',
    meta: {
      icon: 'md-cloud-upload',
      title: '教练员管理'
    },
    component: Main,
    children: [
      {
        path: 'action_page',
        name: '动作类别信息',
        meta: {
          icon: '_smile',
          title: '动作类别信息'
        },
        component: () => import('@/view/coach/index.vue')
      },
      {
        /**
        宗立波
         */
        path: 'action_info_page',
        name: '动作详情',
        meta: {
          icon: 'ios-infinite',
          title: '动作详情',
          hideInMenu: true
        },
        component: () => import('@/view/coach/action.vue')
      },
      {
        /**
        宗立波
         */
        path: 'action_add_page',
        name: '动作类别新增',
        meta: {
          icon: 'md-trending-up',
          title: '动作类别新增',
          hideInMenu: true
        },
        component: () => import('@/view/coach/actionadd.vue')
      },
      {
        path: 'lineup_page',
        name: '上传标准动作',
        meta: {
          icon: '_smile',
          title: '上传标准动作',
        },
        component: () => import('@/view/training/standard.vue')
      }, {
        path: 'dataKing_page',
        name: '训练结果统计',
        meta: {
          icon: '_smile',
          title: '训练结果统计',
        },
        component: () => import('@/view/team/dataKing.vue')
      }
    ]
  },
  { 
    path: '/player',
    name: '运动员管理',
    meta: {
      icon: 'md-cloud-upload',
      title: '运动员管理'
    },
    component: Main,
    children: [
      {
        path: 'playerInfo_page',
        name: '基础动作分析',
        meta: {
          icon: '_smile',
          title: '基础动作分析'
        },
        component: () => import('@/view/training/basic.vue')
      },
      {
        path: 'playerMatch_page',
        name: '训练数据统计',
        meta: {
          icon: '_smile',
          title: '训练数据统计'
        },
        component: () => import('@/view/player/playerMatch.vue')
      }, 
    ]
  },
  {
    
    path: '/system',
    name: '系统维护',
    meta: {
      icon: 'md-cloud-upload',
      title: '系统维护'
    },
    component: Main,
    children: [
      {
        path: 'user_page',
        name: '用户管理',
        meta: {
          icon: '_smile',
          title: '用户管理'
        },
        component: () => import('@/view/users/index.vue')
      },
      {
        /**
        宗立波
         */
        path: 'user_add_page',
        name: '用户新增',
        meta: {
          icon: 'md-trending-up',
          title: '用户新增',
          hideInMenu: true
        },
        component: () => import('@/view/users/useradd.vue')
      },
      {
        /**
        宗立波
         */
        path: 'user_info_page',
        name: '用户详情',
        meta: {
          icon: 'ios-infinite',
          title: '用户详情',
          hideInMenu: true
        },
        component: () => import('@/view/users/user.vue')
      }
    ]
  },
  
]

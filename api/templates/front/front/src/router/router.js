import VueRouter from 'vue-router'

//引入组件
import Index from '../pages'
import Home from '../pages/home/home'
import Login from '../pages/login/login'
import Register from '../pages/register/register'
import Center from '../pages/center/center'
import Messages from '../pages/messages/list'
import Storeup from '../pages/storeup/list'
import News from '../pages/news/news-list'
import NewsDetail from '../pages/news/news-detail'
import yonghuList from '../pages/yonghu/list'
import yonghuDetail from '../pages/yonghu/detail'
import yonghuAdd from '../pages/yonghu/add'
import jingdianxinxiList from '../pages/jingdianxinxi/list'
import jingdianxinxiDetail from '../pages/jingdianxinxi/detail'
import jingdianxinxiAdd from '../pages/jingdianxinxi/add'
import jingdianleixingList from '../pages/jingdianleixing/list'
import jingdianleixingDetail from '../pages/jingdianleixing/detail'
import jingdianleixingAdd from '../pages/jingdianleixing/add'
import jingdianmenpiaoList from '../pages/jingdianmenpiao/list'
import jingdianmenpiaoDetail from '../pages/jingdianmenpiao/detail'
import jingdianmenpiaoAdd from '../pages/jingdianmenpiao/add'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}

//配置路由
export default new VueRouter({
	routes:[
		{
      path: '/',
      redirect: '/index/home'
    },
		{
			path: '/index',
			component: Index,
			children:[
				{
					path: 'home',
					component: Home
				},
				{
					path: 'center',
					component: Center,
				},
				{
					path: 'messages',
					component: Messages
				},
				{
					path: 'storeup',
					component: Storeup
				},
				{
					path: 'news',
					component: News
				},
				{
					path: 'newsDetail',
					component: NewsDetail
				},
				{
					path: 'yonghu',
					component: yonghuList
				},
				{
					path: 'yonghuDetail',
					component: yonghuDetail
				},
				{
					path: 'yonghuAdd',
					component: yonghuAdd
				},
				{
					path: 'jingdianxinxi',
					component: jingdianxinxiList
				},
				{
					path: 'jingdianxinxiDetail',
					component: jingdianxinxiDetail
				},
				{
					path: 'jingdianxinxiAdd',
					component: jingdianxinxiAdd
				},
				{
					path: 'jingdianleixing',
					component: jingdianleixingList
				},
				{
					path: 'jingdianleixingDetail',
					component: jingdianleixingDetail
				},
				{
					path: 'jingdianleixingAdd',
					component: jingdianleixingAdd
				},
				{
					path: 'jingdianmenpiao',
					component: jingdianmenpiaoList
				},
				{
					path: 'jingdianmenpiaoDetail',
					component: jingdianmenpiaoDetail
				},
				{
					path: 'jingdianmenpiaoAdd',
					component: jingdianmenpiaoAdd
				},
			]
		},
		{
			path: '/login',
			component: Login
		},
		{
			path: '/register',
			component: Register
		},
	]
})

const Tabbar = () => import('@/components/Tabbar')

export default [
  {
    path: '/',
    name: 'home',
    components: {
      default: () => import('@/views/home/home'),
      tabbar: Tabbar
    },
    meta: {
      keepAlive: true,
      showHeader: false
    }
  },
  {
    path: '*',
    redirect: {
      name: 'home'
    }
  },
  {
    path: '/news',
    name: 'news',
    components: {
      default: () => import('@/views/home/news/news')
    },
    meta: {
      showHeader: true,
      title: '通知公告'
    }
  },
  {
    path: '/newsDetail',
    name: 'newsDetail',
    components: {
      default: () => import('@/views/home/news/newsDetail')
    },
    meta: {
      showHeader: true,
      title: '公告详情'
    }
  }
]

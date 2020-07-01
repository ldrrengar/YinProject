const Tabbar = () => import('@/components/Tabbar/')

export default [
  {
    path: '/user',
    name: 'user',
    meta: {
      login: true,
      keepAlive: true,
      showHeader: false
    },
    components: {
      default: () => import('@/views/user/user'),
      tabbar: Tabbar
    }
  },
  {
    path: '/withdraw',
    name: 'withdraw',
    meta: {
      showHeader: true,
      title: '提现查询'
    },
    components: {
      default: () => import('@/views/user/withdraw/withdraw')
    }
  },
  {
    path: '/fundDetail',
    name: 'fundDetail',
    meta: {
      showHeader: true,
      title: '资金明细'
    },
    components: {
      default: () => import('@/views/user/fundDetail/fundDetail')
    }
  },
  {
    path: '/myInvitation',
    name: 'myInvitation',
    meta: {
      showHeader: false
    },
    components: {
      default: () => import('@/views/user/myInvitation/myInvitation')
    }
  }
]

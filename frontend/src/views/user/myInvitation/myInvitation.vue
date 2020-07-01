<template>
  <div>
    <van-nav-bar title="我的邀请码" left-text="返回" left-arrow @click-left="goBack" @click-right="downFile" fixed>
      <template #right>
        <van-icon name="leimu" size="18" />
      </template>
    </van-nav-bar>
    <van-image style="margin-top: 44px" src="http://yinzan.net/static/invite/915_20200623102928354930.png" />
  </div>
</template>

<script>
import { NavBar, Image as VanImage } from 'vant'
export default {
    name: 'myInvitation',
    components: {
      [NavBar.name]: NavBar,
      [VanImage.name]: VanImage
    },
    methods: {
      goBack () {
        this.$router.back(-1)
      },
      downFile () {
      }
    }
}
</script>

<style scoped>

</style>

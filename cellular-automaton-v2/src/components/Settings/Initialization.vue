<template>
  <el-form :model="form" label-width="auto" style="max-width: 400px">
    <el-form-item label="x 矩阵长度">
      <el-input v-model="form.x" />
    </el-form-item>
    <el-form-item label="y 矩阵宽度">
      <el-input v-model="form.y" />
    </el-form-item>
    <el-form-item label="采纳 状态数量">
      <el-input v-model="form.initAccept" />
    </el-form-item>
    <el-form-item label="拒绝 状态数量">
      <el-input v-model="form.initRefuse" />
    </el-form-item>
    <el-form-item label="均值 正态分布">
      <el-input v-model="form.mean" />
    </el-form-item>
    <el-form-item label="标准差 正态分布">
      <el-input v-model="form.standardDeviation" />
    </el-form-item>
    <el-form-item label="接受概率">
      <el-input v-model="form.probability" />
    </el-form-item>
    <el-form-item label="生成规则">
      <el-select v-model="form.rule" placeholder="选择规则">
        <el-option label="无干扰下承包商绿色行为的自然蔓延" value="rule1" />
        <el-option label="群体密度不同承包商绿色行为的阻碍蔓延" value="rule2" />
        <el-option label="制度利好下承包商绿色行为的激励蔓延" value="rule3" />
        <el-option label="条件限制下承包商绿色行为的偏好蔓延" value="rule4" />
      </el-select>
    </el-form-item>
    <el-form-item label="迭代次数">
      <el-input v-model="form.iterations" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="initialization">初始化</el-button>
      <el-button type="primary" @click="Go">迭代</el-button>
    </el-form-item>
  </el-form>
</template>

<script lang="ts" setup>
import { reactive } from 'vue'
import { useInitiallization } from '~/stores/initiallization'
import { useData } from '~/stores/data'

import { ElMessage } from 'element-plus'

const initiallization = useInitiallization()
const data = useData()

// do not use same name with ref
const form = reactive(initiallization.initConfig)

const initialization = () => {
  initiallization.updateInitConfig(form)
  data.setInitData(initiallization.initConfig.initAccept, initiallization.initConfig.initRefuse)
  return ElMessage({
    message: 'Initialization finish!',
    type: 'success',
  })
}

const Go = () => {
  console.log(form)
}
</script>
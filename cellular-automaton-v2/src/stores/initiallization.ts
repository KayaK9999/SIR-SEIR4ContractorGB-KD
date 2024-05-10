import { defineStore } from 'pinia'
import { ref, reactive } from 'vue'

import type {InitializationSetting} from '~/lib/utils'

export const useInitiallization = defineStore('init', () => {
  const initConfig = reactive<InitializationSetting>({
    x: 20,
    y: 20,
    initAccept: 2,
    initRefuse: 4,
    mean: 0.6,
    standardDeviation: 0.1,
    probability: 0.6,
    rule: 'rule1',
    iterations: 1,
  })

  const updateInitConfig = (form: InitializationSetting) => {
    for (let key in initConfig) {
      if (initConfig.hasOwnProperty(key) && form.hasOwnProperty(key)) {
        if (key === 'rule') initConfig[key] = form[key]
        else initConfig[key] = Number(form[key])
      }
    }
  }


  return { initConfig, updateInitConfig }
})
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useInitiallization } from '~/stores/initiallization'

export const useData = defineStore('data', () => {
    const initiallization = useInitiallization()
    const initData = ref<number[]>(new Array(initiallization.initConfig.x * initiallization.initConfig.y).fill(0))
    const setInitData = (acceptNum: number, refuseNum: number) => {
        // 随机生成1和-1
        let setAccept = new Set()
        let setRefuse = new Set()
        while (setAccept.size != acceptNum) {
            const i = Math.floor(Math.random() * 40000);
            setAccept.add(i)
        }
        setAccept.forEach((a: any) => {
            initData.value[a] = 1
        })
        while (setRefuse.size != refuseNum) {
            const i = Math.floor(Math.random() * 40000);
            if (!setAccept.has(i)) setRefuse.add(i)
        }
        setRefuse.forEach((a: any) => {
            initData.value[a] = -1
        })
    }

    return { initData, setInitData }
})
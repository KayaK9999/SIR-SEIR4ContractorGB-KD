<template>
    <div class="h-full w-full flex">
        <!-- Setting -->
        <Settings />
        <!-- Dashboard -->
        <div class="h-full flex-1">
            <Dashboard />
        </div>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const activeNames = ref(['1'])
const handleChange = (val: string[]) => {
    console.log(val)
}
</script>

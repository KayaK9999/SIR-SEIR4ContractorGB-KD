<template>
    <div class="h-full w-250px border-r bg-background p-2 lg:w-400px">
        <div class="demo-collapse">
            <el-collapse v-model="activeNames" @change="handleChange">
                <!-- initialization -->
                <el-collapse-item title="Initialization" name="1">
                    <Initialization />
                </el-collapse-item>
                <!-- line -->
                <el-collapse-item title="Line Settings" name="2">
                    <div>
                    </div>
                </el-collapse-item>
                <!-- matrix -->
                <el-collapse-item title="Matrix Settings" name="3">
                    <div>

                    </div>
                </el-collapse-item>
            </el-collapse>
        </div>
    </div>
</template>

<script setup lang="ts">

</script>

<style scoped></style>
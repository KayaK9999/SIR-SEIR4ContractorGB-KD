export interface InitializationSetting {
    x: number,
    y: number,
    initAccept: number,
    initRefuse: number,
    mean: number,
    standardDeviation: number,
    probability: number,
    rule: string,
    iterations: number,
}

export const normalDistribution = function(mean: number, standardDeviation: number) {
    let u = 0, v = 0;
    while (u === 0) u = Math.random(); // 确保 u 不为 0
    while (v === 0) v = Math.random(); // 确保 v 不为 0
  
    const z = Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
    return z * standardDeviation + mean;
}
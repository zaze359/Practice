/**
 * 快速排序的原地分区逻辑
 * 【小于p】【P】【大于p】
 */
fun main() {
    val arrayA = arrayOf(6, 11, 3, 9, 8)
    // 开始位置
    val p = 0
    // 结束位置
    val r = arrayA.size - 1
    println("p:$p; r:$r;")
    // 
    var pivot = arrayA[r]
    println("pivot:$pivot;")
    // i 已处理位置, 表示已匹配到的比pivot小的数据分区的位置
    var i = p
    // j 待处理位置
    for(j in p until r) {
        println("${arrayA[j]}: $pivot")
        if(arrayA[j] < pivot) {
            // 将小于pivot的数据放到已处理分区
            swap(arrayA, i, j)
            i ++
        }
    }
    // 最后将pivot放到 左右分区之间。
    swap(arrayA, i, r)

    arrayA.forEach {
        println("$it")
    }
}

fun swap(array : Array<Int>, i: Int, j:Int) {
    if(i == j) return
    val temp = array[i]
    array[i] = array[j]
    array[j] = temp
}
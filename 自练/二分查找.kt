/**
 * 二分查找练习
 * 顺序表结构且 数据有序。
 */
fun main() {
    val a = arrayOf(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
    val value = 11
    val n = a.size
    println("bsearch: ${bsearch(a, n, value)}")
    println("bsearchInternally: ${bsearchInternally(a, 0, n - 1, value)}")

}

/**
 * 非递归实现
 */
fun bsearch(a: Array<Int>, n: Int, value: Int) : Int {
    var low = 0
    var high = n - 1
    while(low <= high) {
        val mid = (low + high) / 2
        if(a[mid] == value) {
            return mid
        } else if(a[mid] > value) {
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    return -1
}

/**
 * 递归
 */
fun bsearchInternally(a: Array<Int>, low: Int, high: Int, value: Int) : Int { 
    if(low > high) {
        return -1
    }
    val mid: Int = (low + high) / 2
    return if(a[mid] == value) {
        mid
    } else if(a[mid] > value){
        bsearchInternally(a, low, mid - 1, value)
    } else {
        bsearchInternally(a, mid + 1, high, value)
    }
}
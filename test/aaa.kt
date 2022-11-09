
fun main() {
    var a = 0
    var b = 1
    // val b = a++
    println("${a} : ${b}")
    A a = A(10)
    
}

class A {
    private A as[];

    A(int level) {
        as = A[level]
    }
}
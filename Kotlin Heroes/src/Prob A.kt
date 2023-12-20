import java.util.*

fun sum(a: Int, b: Int): Int{
   return a+b;
}

fun main(){
    val scanner= Scanner(System.`in`)
    for(i:Int in 1 .. scanner.nextInt())
    println(sum(scanner.nextInt(),scanner.nextInt()))
}
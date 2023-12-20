import java.util.*
import kotlin.collections.ArrayList
import kotlin.math.round

fun isRound(a:Int){
    var num=10
    var i=a
    var arr= ArrayList<Int>()
    while(i>0){
        if(i%num!=0){
            var b=i%num
            arr.add(b)
            i-=b
        }
        num*=10
    }
    println(arr.size)
    print(arr.joinToString(" "))
}

fun main(){
    val scanner= Scanner(System.`in`)
    for(i:Int in 1 .. scanner.nextInt()) {
        isRound(scanner.nextInt());
        println()
    }
}
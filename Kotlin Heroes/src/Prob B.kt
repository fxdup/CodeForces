import java.util.*
import kotlin.math.max

fun square(a1:Int, b1:Int, a2:Int, b2:Int):Boolean{
    if(a1== max(a1,b1) && a1==a2)
        return a1==b1+b2
    else if(a1== max(a1,b1) &&a1==b2)
        return a1==b1+a2
    else if(b1== max(a1,b1) &&b1==a2)
        return b1==a1+b2
    else if(b1== max(a1,b1) &&b1==b2)
        return b1==a1+a2
    return false
}

fun main(){
    val scan= Scanner(System.`in`)
    for(i:Int in 1..scan.nextInt())
            if (square(scan.nextInt(), scan.nextInt(), scan.nextInt(), scan.nextInt()))
                println("yes")
            else println("no")
}
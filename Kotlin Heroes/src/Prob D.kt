import java.util.*
import kotlin.collections.ArrayList

fun main(){
    val scanner= Scanner(System.`in`)
    for(t:Int in 1 .. scanner.nextInt()) {
        var arr=ArrayList<Int>()
        for(i:Int in 1..scanner.nextInt()){
            arr.add(scanner.nextInt())
        }
        var lastSum=0
        var sumi=0
        var sumj=0
        var sum=0
        var turn=true
        var count=1
        while(arr.size>0){
            if(turn){
                var i = arr.get(0)
                arr.removeAt(0)
                sumi+=i
                sum+=i
            }else{
                var j = arr.get(arr.lastIndex)
                arr.removeAt(arr.lastIndex)
                sumj+=j
                sum+=j
            }
            if(lastSum<sum){
                if(arr.size!=0)
                    count++
                turn=!turn
                lastSum=sum
                sum=0
            }
        }
        println("$count $sumi $sumj")


    }
}
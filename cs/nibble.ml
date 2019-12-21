(* Extracting nibbles a functional guide 
 * Given a 31-bit ocaml integer we want to extract the nibbles :
 * The order is reversed so 0 is the index of LSN (left-most significant nibble)
 * So to extract the nibbles from 0xef = 0111 1111 
 * We shift 0xef to the right by (index * 2) where index = 0
 * This will output "f" the right most nibble in the 0xef which is 239 in decimal 
 *
*)


let nibble a index =((a lsr (index lsl 2)) land 0xf)

let () =
    
    let a = 0xFE123456 in    
    let b  = nibble a 0  in
    Printf.printf "%x\n" b ;
    let c = nibble a 1 in   
    Printf.printf "%x\n" c;

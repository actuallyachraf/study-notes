let nibble a index =((a lsr (index lsl 2)) land 0xf)

let () =
    
    let a = 0xFE123456 in    
    let b  = nibble a 0  in
    Printf.printf "%x\n" b ;
    let c = nibble a 1 in   
    Printf.printf "%x\n" c;

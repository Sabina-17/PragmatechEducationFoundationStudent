console.log()


function Foo(a, b) {
    console.log(a + b)
}



function Bar(...nums) {
    let cem = 0;
    for (i = 0; i < nums.length; i++) {
        cem += nums[i]
    }

    console.log(cem)
}

Bar(1, 7, 45, 12, 67, 12, 78, 89)
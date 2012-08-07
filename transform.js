function transform()
{
    var size = 128000;
    var a = 2.0;
    var b = 0.5;
    var c = 0.1;
    var d = 0.5
    var e = 2.0;
    var f = 0.1;

    var data = [];
    var sum = 0.0;

    for (var i = 0; i < size; ++i) {
        var x = i;
        var y = i;
        var X = a*x + c*y + e;
        var Y = b*x + d*y + f;
        data.push([X, Y]);
        sum += X;
    }

    return sum;
}

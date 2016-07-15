polulatePhone = function (area, start, stop){
    for (var i=start; i < stop; i++){
        var country = 1 + (( Math.random() * 8) << 0);
        var num = (country * 1e10) + (area * 1e7) + i;
        db.phone.insert({
            _id:num,
            display: "+" + country + " " + area + "-" + i,
            components: {
                country: country,
                area: area,
                prefix: (i * 1e-4) << 0,
                num: i
            },
        });
    }
}
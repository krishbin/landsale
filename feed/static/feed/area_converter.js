function areaconvert(input_area,input_unit,output_unit){
    var output_area = input_area;
    //For BG
    if(input_unit === "BG" && output_unit === "KT"){
        output_area = Number(input_area) * 20;
    }
    else if(input_unit === "BG" && output_unit === "SM"){
        output_area = Number(input_area) * 6772.63;
    }
    else if(input_unit === "BG" && output_unit === "SF"){
        output_area = Number(input_area) * 72900;
    }
    else if(input_unit === "BG" && output_unit === "RO"){
        output_area = Number(input_area) * 13.31;
    }
    else if(input_unit === "BG" && output_unit === "AN"){
        output_area = Number(input_area) * 212.96;
    }

    //For KT
    if(input_unit === "KT" && output_unit === "SM"){
        output_area = Number(input_area) * 338.6315;
    }
    else if(input_unit === "KT" && output_unit === "SF"){
        output_area = Number(input_area) * 3645;
    }
    else if(input_unit === "KT" && output_unit === "RO"){
        output_area = Number(input_area) * 0.6655;
    }
    else if(input_unit === "KT" && output_unit === "AN"){
        output_area = Number(input_area) * 10.648;
    }
    else if(input_unit === "KT" && output_unit === "BG"){
        output_area = Number(input_area) * 0.05;
    }


    //For SM
    if(input_unit === "SM" && output_unit === "KT"){
        output_area = Number(input_area) * 0.00295;
    }
    else if(input_unit === "SM" && output_unit === "SF"){
        output_area = Number(input_area) * 10.76391;
    }
    else if(input_unit === "SM" && output_unit === "RO"){
        output_area = Number(input_area) * 0.00196;
    }
    else if(input_unit === "SM" && output_unit === "AN"){
        output_area = Number(input_area) * 0.03144;
    }
    else if(input_unit === "SM" && output_unit === "BG"){
        output_area = Number(input_area) * 0.000395;
    }


    //For SF
    if(input_unit === "SF" && output_unit === "KT"){
        output_area = Number(input_area) * 0.000274;
    }
    else if(input_unit === "SF" && output_unit === "SM"){
        output_area = Number(input_area) * 0.0929;
    }
    else if(input_unit === "SF" && output_unit === "RO"){
        output_area = Number(input_area) * 0.000182;
    }
    else if(input_unit === "SF" && output_unit === "AN"){
        output_area = Number(input_area) * 0.00292;
    }
    else if(input_unit === "SF" && output_unit === "BG"){
        output_area = Number(input_area) * 0.0000137;
    }

    //For RO
    if(input_unit === "RO" && output_unit === "KT"){
        output_area = Number(input_area) * 1.5026;
    }
    else if(input_unit === "RO" && output_unit === "SM"){
        output_area = Number(input_area) * 508.837;
    }
    else if(input_unit === "RO" && output_unit === "SF"){
        output_area = Number(input_area) * 5477.0849;
    }
    else if(input_unit === "RO" && output_unit === "AN"){
        output_area = Number(input_area) * 16;
    }
    else if(input_unit === "RO" && output_unit === "BG"){
        output_area = Number(input_area) * 0.07513;
    }


    //For AN
    if(input_unit === "AN" && output_unit === "KT"){
        output_area = Number(input_area) * 0.09391;
    }
    else if(input_unit === "AN" && output_unit === "SM"){
        output_area = Number(input_area) * 31.8023;
    }
    else if(input_unit === "AN" && output_unit === "SF"){
        output_area = Number(input_area) * 342.3178;
    }
    else if(input_unit === "AN" && output_unit === "RO"){
        output_area = Number(input_area) * 0.0625;
    }
    else if(input_unit === "AN" && output_unit === "BG"){
        output_area = Number(input_area) * 0.004695;
    }

    return output_area.toFixed(4);
}

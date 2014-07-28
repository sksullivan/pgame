 #version 330 core
in vec3 rgbout;
in vec3 rgboffout;
in vec4 gl_FragCoord;
in vec2 timeout;
out vec4 fragColor;
void main() {
	//fragColor = vec4(rgbout.x, rgbout.y, rgbout.z, 1);
	//fragColor = vec4(gl_FragCoord.x/640.0, gl_FragCoord.y/480.0, 100, 1);
	/*int offset = int(gl_FragCoord.y)+int(rgbout.x);
	if (offset % 6 == 0 || offset % 6 == 1 || offset % 6 == 2) {
		fragColor = vec4(0,0,0,1);
	} else {
		//fragColor = vec4(gl_FragCoord.x/255+float(rgbout.x),gl_FragCoord.y/255,1,1);
		fragColor = vec4(1,1,1,1);
	}*/
	vec4 white = vec4(1,1,1,1);
	vec4 black = vec4(0,0,0,1);
	float stripeWidth = 10;
	float x = (gl_FragCoord.x-1440/2)/timeout.x;
	float y = (gl_FragCoord.y-900/2)/timeout.x;
	// if (x*x+y*y < rgbout.x*rgbout.x) {
	// 	if (x*x+y*y > (rgbout.x-stripeWidth)*(rgbout.x-stripeWidth)) {
	// 		fragColor = black;
	// 	} else {
	// 		fragColor = white;
	// 	}
	// } else {
	// 	fragColor = white;
	// }

	// if (int((x*x+y*y)/rgbout.x) % 2 == 0) { // OH GOD THE CIRCLES
	// 	fragColor = black;
	// } else {
	// 	fragColor = white;
	// }

	vec4 fragColor1;
	vec4 fragColor2;

	vec4 color = vec4(rgbout.x,rgbout.y,rgbout.z,1);
	vec4 anticolor = vec4(1-rgbout.x,1-rgbout.y,1-rgbout.z,1);
	vec4 offsetColor = vec4(rgboffout.x,rgboffout.y,rgboffout.z,1);

	if (int((x*x+y*y)/(timeout.x)) % 5 == 0) { // OH GOD THE CIRCLES PART 2
		fragColor1 = color;
	} else {
		//vec4 color = vec4(rgbout.x,rgbout.y,rgbout.z,1);
		fragColor1 = offsetColor;
		//fragColor = white;
	}



	//vec2 z;
    //z.x = 3.0 * (gl_TexCoord[0].x - 0.5);
    //z.y = 2.0 * (gl_TexCoord[0].y - 0.5);

	//how about a one liner? - CARPET THAT ATTACKS
	fragColor2 = vec4(sin(x),sin(y),rgbout.z,1.0);

	// if (int(x/y*360) > int(tan(timeout.x/5)*360)) { // PINWHEEL LOL MOFO
	// 	vec4 anticolor = vec4(1-rgbout.x,1-rgbout.y,1-rgbout.z,1);
	// 	fragColor = anticolor;
	// } else {
	// 	vec4 color = vec4(rgbout.x,rgbout.y,rgbout.z,1);
	// 	fragColor = color;
	// }

	// if (((int(x/y*360) / 6) % 2 == 0)) { // HOLY PATTERNS BATMAN
	// 	vec4 anticolor = vec4(1-rgbout.x,1-rgbout.y,1-rgbout.z,1);
	// 	fragColor = anticolor;
	// } else {
	// 	vec4 color = vec4(rgbout.x,rgbout.y,rgbout.z,1);
	// 	fragColor = color;
	// }

	float scale = gl_FragCoord.x/1440;
	fragColor = vec4(fragColor1.x*scale+fragColor2.x*(1-scale),fragColor1.y*scale+fragColor2.y*(1-scale),fragColor1.z*scale+fragColor2.z*(1-scale),1.0);

	// if (((int(x/y*360) / 120) % 2 == 0)) { // A SEIZURE A DAY
	// 	vec4 anticolor = vec4(1-rgbout.x,1-rgbout.y,1-rgbout.z,1);
	// 	fragColor = anticolor;
	// } else {
	// 	vec4 color = vec4(rgbout.x,rgbout.y,rgbout.z,1);
	// 	fragColor = color;
	// }
}
 #version 330 core
in vec3 rgbout;
in vec3 rgboffout;
in vec4 gl_FragCoord;
in vec2 timeout;
out vec4 fragColor;
void main() {
	float x = (gl_FragCoord.x-1440/2)/timeout.x;
	float y = (gl_FragCoord.y-900/2)/timeout.x;

	vec4 color = vec4(rgbout.x,rgbout.y,rgbout.z,1);
	vec4 anticolor = vec4(1-rgbout.x,1-rgbout.y,1-rgbout.z,1);
	vec4 offsetColor = vec4(rgboffout.x,rgboffout.y,rgboffout.z,1);

	if (sin((x*x+y*y)+timeout.x) > 0) { // OH GOD THE CIRCLES PART 2
		fragColor = color;
	} else {
		fragColor = offsetColor;
	}
}
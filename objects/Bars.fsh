 #version 330 core
in vec3 rgbout;
in vec3 rgboffout;
in vec4 gl_FragCoord;
in vec2 timeout;
out vec4 fragColor;
void main() {
	float x = (gl_FragCoord.x-1440/2)/timeout.x/(cos(timeout.x)+1.5);
	float y = (gl_FragCoord.y-900/2)/timeout.x/(sin(timeout.x)+1.5);

	vec4 color = vec4(rgbout.x,rgbout.y,rgbout.z,1);
	vec4 anticolor = vec4(1-rgbout.x,1-rgbout.y,1-rgbout.z,1);
	vec4 offsetColor = vec4(rgboffout.x,rgboffout.y,rgboffout.z,1);

	fragColor = vec4(sin(x),sin(y),rgbout.z,1.0);
}
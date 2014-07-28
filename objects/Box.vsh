#version 330 core
layout(location = 0) in vec4 position;
uniform vec2 rg;
uniform vec2 time;
uniform vec2 b;
uniform vec2 rgoff;
uniform vec2 boff;
out vec3 rgbout;
out vec3 rgboffout;
out vec2 timeout;

void main() {
	//gl_Position = vec4(position.x+mouse.x, position.y+mouse.y, position.z, position.w);
	gl_Position = vec4(position.x, position.y, position.z, position.w);
	rgbout = vec3(rg.x,rg.y,b.x);
	rgboffout = vec3(rgoff.x,rgoff.y,boff.x);
	timeout = time;
}
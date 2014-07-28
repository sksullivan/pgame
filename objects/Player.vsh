#version 330 core
layout(location = 0) in vec4 position;
uniform vec2 self;
void main() {
	gl_Position = vec4(position.x+self.x, position.y+self.y, position.z, position.w);
}
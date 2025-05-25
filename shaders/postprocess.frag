#version 330 core

in vec2 uv;
out vec4 fragColor;

uniform sampler2D u_texture;

void main() {
    vec4 texColor = texture(u_texture, uv);
    fragColor = vec4(texColor);
}

#version 330 core

in vec2 uv;
out vec4 fragColor;

uniform sampler2D u_texture;

#define FXAA_SPAN_MAX 8.0
#define FXAA_REDUCE_MUL 1.0/8.0
#define FXAA_REDUCE_MIN 1.0/128.0

void main() {
    vec2 invResolution = 1.0 / vec2(textureSize(u_texture, 0));
    
    vec4 texColor = texture(u_texture, uv);
    float brightness = 1.2; 
    vec3 currentLuma = texColor.rgb * brightness;

    vec3 luma = vec3(0.299, 0.587, 0.114);

    float lumaNW = dot(texture(u_texture, uv + vec2(-1.0, -1.0) * invResolution).rgb * brightness, luma);
    float lumaNE = dot(texture(u_texture, uv + vec2( 1.0, -1.0) * invResolution).rgb * brightness, luma);
    float lumaSW = dot(texture(u_texture, uv + vec2(-1.0,  1.0) * invResolution).rgb * brightness, luma);
    float lumaSE = dot(texture(u_texture, uv + vec2( 1.0,  1.0) * invResolution).rgb * brightness, luma);
    float lumaM  = dot(currentLuma, luma);

    float lumaMin = min(lumaM, min(min(lumaNW, lumaNE), min(lumaSW, lumaSE)));
    float lumaMax = max(lumaM, max(max(lumaNW, lumaNE), max(lumaSW, lumaSE)));

    float range = lumaMax - lumaMin;

    if (range < max(FXAA_REDUCE_MIN, lumaMax * FXAA_REDUCE_MUL)) {
        fragColor = vec4(currentLuma, texColor.a);
        return;
    }

    vec2 dir;
    dir.x = -((lumaNW + lumaNE) - (lumaSW + lumaSE));
    dir.y =  ((lumaNW + lumaSW) - (lumaNE + lumaSE));

    float dirReduce = max((lumaNW + lumaNE + lumaSW + lumaSE) * 0.25 * FXAA_REDUCE_MUL, FXAA_REDUCE_MIN);
    float rcpDirMin = 1.0 / (min(abs(dir.x), abs(dir.y)) + dirReduce);

    dir = min(vec2(FXAA_SPAN_MAX, FXAA_SPAN_MAX), max(vec2(-FXAA_SPAN_MAX, -FXAA_SPAN_MAX), dir * rcpDirMin)) * invResolution;

    vec3 rgbA = 0.5 * (
        texture(u_texture, uv + dir * (1.0/3.0 - 0.5)).rgb * brightness +
        texture(u_texture, uv + dir * (2.0/3.0 - 0.5)).rgb * brightness);
    
    vec3 rgbB = rgbA * 0.5 + 0.25 * (
        texture(u_texture, uv + dir * -0.5).rgb * brightness +
        texture(u_texture, uv + dir * 0.5).rgb * brightness);

    fragColor = vec4(rgbB, texColor.a);
}
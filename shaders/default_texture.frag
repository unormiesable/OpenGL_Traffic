// INI SHADER DEFAULT JIKA OBJEK TIDAK MENGGUNAKAN TEXTURE

#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;
in vec4 shadowCoord;

struct Light {
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;
uniform sampler2DShadow shadowMap;
uniform vec2 u_resolution;
uniform bool u_enableShadow;
uniform bool u_enableAO;
uniform float shadowBlur;
uniform float new_shade;
uniform float ao_factor;
uniform float AOBlur;

// PCF SETUP ========================================================
// DAH NEMU SOFT SHADOW JADI GA DIPAKE
float pcfLookup(vec2 offset) {
    float size = 1.0 / u_resolution.x;
    return textureProj(shadowMap, shadowCoord + vec4(offset * size, 0.0, 0.0));
}

float getPCFShadow() {
    float shadow = 0.0;
    vec2 offsets[4] = vec2[4](vec2(-1.0, -1.0), vec2(1.0, -1.0), vec2(-1.0, 1.0), vec2(1.0, 1.0));
    for (int i = 0; i < 4; i++) {
        shadow += pcfLookup(offsets[i]);
    }
    return shadow / 16.0;
}

// SOFT SHADOW SETUP =================================================
float lookup(float ox, float oy) {
    vec2 pixelOffset = 1 / u_resolution;
    return textureProj(shadowMap, shadowCoord + vec4(ox * pixelOffset.x * shadowCoord.w,
                                                     oy * pixelOffset.y * shadowCoord.w, 0.0, 0.0));
}

float getSoftShadow() {
    float shadow;
    float step_width = 0.01 * shadowBlur;
    float extend = step_width * 3.0 + step_width / 2.0;
    for (float y = -extend; y <= extend; y += step_width) {
        for (float x = -extend; x <= extend; x += step_width) {
            shadow += lookup(x, y);
        }
    }
    return shadow / 128;
}

// SETUP AO (TAPI MASIH SHADOW BASED) - (BELUM BERJALAN SESUAI RENCANA) - (TAPI MENGHASILKAN BETTER SHADOW)
float getFakeAo() {
    float shadow;
    float step_width = 0.5 * AOBlur;
    float extend = step_width * 3.0 + step_width / 2.0;
    for (float y = -extend; y <= extend; y += step_width) {
        for (float x = -extend; x <= extend; x += step_width) {
            shadow += lookup(x, y);
        }
    }
    return shadow / 256;
}


// LIGHTING ===========================================================
vec3 getLight(vec3 color) {
    vec3 Normal = normalize(normal);

    // AMBIENT (IA)
    vec3 ambient = light.Ia;

    // DIFFUSE (ID)
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * light.Id;

    // SPECULAR (IS)
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 64);
    vec3 specular = spec * light.Is;

    // SHADOW
    float shadow = u_enableShadow ? getSoftShadow() : 1.0;
    
    // FAKE AO (BELUM BERJALAN SESUAI RENCANA) (TAPI MENGHASILKAN BETTER SHADOW)
    float ao = u_enableAO ? getFakeAo() * ao_factor : 1.0;

    // FINAL
    return color * (ambient +((diffuse + (shadow * new_shade)) + specular) * (shadow + (ao)));
}

// MAIN ===============================================================
void main() {
    float gamma = 2.2;
    vec3 color = texture(u_texture_0, uv_0).rgb;

    color = getLight(color);

    color = pow(color, 1.0 / vec3(gamma)); 
    fragColor = vec4(color, 1.0);
}

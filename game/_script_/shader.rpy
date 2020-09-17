init python:
    renpy.register_shader("gaussianblur", variables="""
        uniform sampler2D tex0;
        uniform float u_radius;
    """, fragment_functions="""
        float SCurve (float x) {
            x = x * 2.0 - 1.0;
            return dot(vec3(-x, 2.0, 1.0 ), vec3(abs(x), x, 1.0)) * 0.5;
        }

        vec4 BlurH(sampler2D source, vec2 size, vec2 uv, float radius) {
            if (radius >= 1.0)
            {
                vec4 A = vec4(0.0);
                vec4 C = vec4(0.0);

                float width = 1.0 / size.x;

                float divisor = 0.0;
                float weight = 0.0;

                float radiusMultiplier = 1.0 / radius;

                for (float x = -radius; x <= radius; x++)
                {
                    A = texture2D(source, uv + vec2(x * width, 0.0));

                    weight = SCurve(1.0 - (abs(x) * radiusMultiplier));

                    C += A * weight;

                    divisor += weight;
                }

                return vec4(C.rgb / divisor, 1.0);
            }

            return texture2D(source, uv);
        }
    """, fragment_700="""
        vec2 iRes = vec2(1080.0, 600.0);
        vec2 uv = v_tex_coord.st;

        gl_FragColor = BlurH(tex0, iRes.xy, uv, u_radius);
        """)

transform gaussianblur(radius=15.0):
    mesh True
    shader "gaussianblur"
    u_radius radius

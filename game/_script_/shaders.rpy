init python:
    renpy.register_shader("outline_shader", fragment_300="""
        const float THICKNESS = 1.0 / 128.0;
        vec4 col = texture2D(tex0, v_tex_coord);

        if (col.a <= 0.5) {
            float a = texture2D(tex0, vec2(v_tex_coord.x + THICKNESS, v_tex_coord.y)).a +
            texture2D(tex0, vec2(v_tex_coord.x, v_tex_coord.y - THICKNESS)).a +
            texture2D(tex0, vec2(v_tex_coord.x - THICKNESS, v_tex_coord.y)).a +
            texture2D(tex0, vec2(v_tex_coord.x, v_tex_coord.y + THICKNESS)).a;

            if (col.a < 1.0 && a > 0.0)
                gl_FragColor = vec4(0.0, 1.0, 0.0, 0.8);
            else
                gl_FragColor = col;
        }
    """)

import streamlit as st
from io import StringIO

st.set_page_config(page_title="STALKER RTac Official Site", layout="wide", initial_sidebar_state="expanded", page_icon="STALKER RTac Logo.png")

@st.cache_data()
def showScreenshots(screenshots, ext):
    for img in screenshots:
        st.image(img+ext, img)

page = st.sidebar.radio("**Navigation:**", ["STALKER RTac", "Miracle Graphics Pack", "MCM Settings For SSS", "ReShade File Finder", "Atmospheric Preset Editor"])
atmospresetlist = ["Realistic", "Cinematic", "Dramatic", "Vibrant", "Dull", "Warm", "Cold", "Summer", "Autumn", "Late Fall", "Winter", "Nature", "Gloomy", "Mysterious", "Apocalypse", "Horror", "Night", "NaturalNV"]
atmospresets = {
    
    "Apocalypse": """r__color_grading (0, 0, 0)

r__saturation 0.9
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.600000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.050000)
shader_param_3 (0.020000, 0.000000, 0.050000, 0.650000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Autumn": """r__color_grading (0, 0, 0)

r__saturation 0.9
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.030000)
shader_param_3 (0.000000, 0.030000, 0.060000, 0.630000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Cinematic": """r__color_grading (0, 0, 0)

r__saturation 0.9
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.050000)
shader_param_3 (0.020000, 0.015000, 0.000000, 0.740000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.300000)
""",
    
    "Cold": """r__color_grading (0, 0, 0)

r__saturation 0.8
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.030000)
shader_param_3 (0.040000, 0.030000, 0.000000, 0.610000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Dramatic": """r__color_grading (0, 0, 0)

r__saturation 1.
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.800000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.000000)
shader_param_3 (0.000000, 0.000000, 0.000000, 0.75000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.000000)
""",
    
    "Dull": """r__color_grading (0, 0, 0)

r__saturation 0.7
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.030000)
shader_param_3 (0.030000, 0.020000, 0.000000, 0.630000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Gloomy": """r__color_grading (0, 0, 0)

r__saturation 0.7
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.030000)
shader_param_3 (0.080000, 0.050000, 0.000000, 0.600000)
shader_param_3 (0.050000, 0.045000, 0.000000, 0.620000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Horror": """r__color_grading (0, 0, 0)

r__saturation 0.7
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.800000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.030000)
shader_param_3 (0.000000, 0.030000, 0.050000, 0.750000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.300000)
""",
    
    "Late Fall": """r__color_grading (0, 0, 0)

r__saturation 0.9
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.030000)
shader_param_3 (0.000000, 0.020000, 0.060000, 0.630000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Mysterious": """r__color_grading (0, 0, 0)

r__saturation 0.9
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.600000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.050000)
shader_param_3 (0.070000, 0.055000, 0.000000, 0.640000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)""",
    
    "NaturalNV": """r__color_grading (0, 0, 0)

r__saturation 0.5
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.150000)
shader_param_3 (0.200000, 0.100000, 0.000000, 0.600000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.000000)
""",
    
    "Nature": """r__color_grading (0, 0, 0)

r__saturation 1.1
r__gamma 1
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.600000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.050000)
shader_param_3 (0.010000, 0.005000, 0.000000, 0.650000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Night": """r__color_grading (0, 0, 0)

r__saturation 0.75
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.600000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.100000)
shader_param_3 (0.000000, 0.000000, 0.000000, 0.650000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Realistic": """r__color_grading (0, 0, 0)

r__saturation 0.85
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.030000)
shader_param_3 (0.000000, 0.010000, 0.030000, 0.620000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Summer": """r__color_grading (0, 0, 0)

r__saturation 1.
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.030000)
shader_param_3 (0.030000, 0.020000, 0.000000, 0.630000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Vibrant": """r__color_grading (0, 0, 0)

r__saturation 1.2
r__gamma 1
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.050000)
shader_param_3 (0.000000, 0.000000, 0.000000, 0.650000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Warm": """r__color_grading (0, 0, 0)

r__saturation 0.9
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.000000, 0.000000, 0.030000)
shader_param_3 (0.000000, 0.030000, 0.070000, 0.610000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.200000)
""",
    
    "Winter": """r__color_grading (0, 0, 0)

r__saturation 0.85
r__gamma 1.
r__exposure 1.
scope_factor 1

r2_gloss_factor 0.001
r2_gloss_min 0.56
r2_sun_lumscale 1.5
r2_sun_lumscale_amb 1.
r2_sun_lumscale_hemi 1.
r2_tonemap on
r2_tonemap_adaptation 3.
r2_tonemap_amount 1.
r2_tonemap_lowlum 0.1
r2_tonemap_middlegray 1.
rs_c_brightness 1
rs_c_contrast 1
rs_c_gamma 1.
r2_sun_depth_near_scale 0.9998
r2_sun_depth_far_scale 0.99988
r2_sun_tsm_bias 0
ssfx_hud_hemi 0

shader_param_1 (0.000000, 0.000000, 0.000000, 0.700000)
shader_param_2 (0.000000, 0.005000, 0.010000, 0.025000)
shader_param_3 (0.050000, 0.025000, 0.000000, 0.680000)
shader_param_4 (0.000000, 0.000000, 0.000000, 1.000000)
"""

}
sssmcm = """
![mcm]
        ssfx_module/ao/blur_mcm          = 1
        ssfx_module/ao/distance_mcm      = 150
        ssfx_module/ao/flora_int_mcm     = 1
        ssfx_module/ao/global_int_mcm    = 1
        ssfx_module/ao/hud_int_mcm       = 1
        ssfx_module/ao/max_occ_mcm       = 0.1
        ssfx_module/ao/quality_mcm       = 4
        ssfx_module/ao/radius_mcm        = 1.9
        ssfx_module/ao/res_mcm           = 1
        ssfx_module/florafixes/grass_specular_mcm = 0.15
        ssfx_module/florafixes/grass_specular_wet_mcm = 0.18
        ssfx_module/florafixes/sss_color_mcm = 0.38
        ssfx_module/florafixes/sss_int_mcm = 4.6
        ssfx_module/florafixes/trees_specular_mcm = 0.14
        ssfx_module/florafixes/trees_specular_wet_mcm = 0.15
        ssfx_module/fog/density_mcm      = 1.5
        ssfx_module/fog/height_mcm       = 15
        ssfx_module/fog/scattering_mcm   = 0.75
        ssfx_module/fog/suncolor_mcm     = 0.11
        ssfx_module/general/shaderscope_patch_mcm = true
        ssfx_module/il/blur_mcm          = 0.5
        ssfx_module/il/distance_mcm      = 150
        ssfx_module/il/flora_int_mcm     = 1
        ssfx_module/il/global_int_mcm    = 4
        ssfx_module/il/hud_int_mcm       = 1
        ssfx_module/il/quality_mcm       = 24
        ssfx_module/il/res_mcm           = 0.15
        ssfx_module/il/vibrance_mcm      = 0.6
        ssfx_module/inter_grass/anomalies_distance_mcm = 20
        ssfx_module/inter_grass/enable_anomalies_mcm = true
        ssfx_module/inter_grass/enable_mcm = true
        ssfx_module/inter_grass/enable_mutants_mcm = true
        ssfx_module/inter_grass/enable_player_mcm = true
        ssfx_module/inter_grass/explosions_speed_mcm = 5
        ssfx_module/inter_grass/explosions_str_mcm = 1
        ssfx_module/inter_grass/horizontal_str_mcm = 2.5
        ssfx_module/inter_grass/max_distance_mcm = 750
        ssfx_module/inter_grass/max_entities_mcm = 3
        ssfx_module/inter_grass/radius_mcm = 1
        ssfx_module/inter_grass/shooting_range_mcm = 2
        ssfx_module/inter_grass/shooting_str_mcm = 0.3
        ssfx_module/inter_grass/vertical_str_mcm = 2.5
        ssfx_module/parallax/ao_mcm      = 0.5
        ssfx_module/parallax/height_mcm  = 0.035
        ssfx_module/parallax/quality_mcm = 16
        ssfx_module/parallax/range_mcm   = 12
        ssfx_module/parallax/refine_mcm  = false
        ssfx_module/shadows/lod_max_mcm  = 0
        ssfx_module/shadows/lod_min_mcm  = 3
        ssfx_module/shadows/lod_quality_mcm = 0.5
        ssfx_module/shadows/volumetric_force_mcm = true
        ssfx_module/shadows/volumetric_int_mcm = 1
        ssfx_module/shadows/volumetric_quality_mcm = 3
        ssfx_module/shw_cascades/grass_shw_distance_mcm = 100
        ssfx_module/shw_cascades/grass_shw_nondir_maxdistance_mcm = 50
        ssfx_module/shw_cascades/grass_shw_quality_mcm = 0
        ssfx_module/shw_cascades/size_1_mcm = 10
        ssfx_module/shw_cascades/size_2_mcm = 50
        ssfx_module/shw_cascades/size_3_mcm = 300
        ssfx_module/ssfx_pp/ssfx_bloom/blur_mcm = 5
        ssfx_module/ssfx_pp/ssfx_bloom/dirt_mcm = 0
        ssfx_module/ssfx_pp/ssfx_bloom/exposure_mcm = 1
        ssfx_module/ssfx_pp/ssfx_bloom/lens_mcm = 0
        ssfx_module/ssfx_pp/ssfx_bloom/sky_mcm = 0
        ssfx_module/ssfx_pp/ssfx_bloom/threshold_mcm = 9.5
        ssfx_module/ssfx_pp/ssfx_bloom/use_weather_mcm = false
        ssfx_module/ssfx_pp/ssfx_bloom/vibrance_mcm = 1.3
        ssfx_module/ssfx_pp/ssfx_motionblur/camera_mcm = 1
        ssfx_module/ssfx_pp/ssfx_motionblur/hudonly_mcm = false
        ssfx_module/ssfx_pp/ssfx_motionblur/intensity_mcm = 0.5
        ssfx_module/ssfx_pp/ssfx_motionblur/quality_mcm = 8
        ssfx_module/ssfx_pp/ssfx_taa/enabled_mcm = true
        ssfx_module/ssfx_pp/ssfx_taa/jitter_mcm = 0.5
        ssfx_module/ssfx_pp/ssfx_taa/sharpness_mcm = 0
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/jump_vol_mcm = 0.7
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/land_vol_mcm = 0.7
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/main_vol_mcm = 0.4
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/multi_no_rain_mcm = 0.3
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/multi_run_mcm = 1.4
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/multi_walk_mcm = 0.33
        ssfx_module/ssfx_rain_module/ssfx_rain_footsteps/vol_rnd_mcm = 0.15
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/animation_speed_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/buildup_mcm = 2
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/density_mcm = 2
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/drying_mcm = 0.5
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/extra_gloss_mcm = 0.4
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/gloss_mcm = 2
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/reflection_str_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/refraction_str_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_hud_raindrops/size_mcm = 0.5
        ssfx_module/ssfx_rain_module/ssfx_rain_main/alpha_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_main/brightness_mcm = 0.2
        ssfx_module/ssfx_rain_module/ssfx_rain_main/len_mcm = 1
        ssfx_module/ssfx_rain_module/ssfx_rain_main/max_drops_mcm = 3000
        ssfx_module/ssfx_rain_module/ssfx_rain_main/quality_mcm = 0
        ssfx_module/ssfx_rain_module/ssfx_rain_main/radius_mcm = 15
        ssfx_module/ssfx_rain_module/ssfx_rain_main/reflection_mcm = 0.6
        ssfx_module/ssfx_rain_module/ssfx_rain_main/refraction_mcm = 3
        ssfx_module/ssfx_rain_module/ssfx_rain_main/speed_mcm = 2
        ssfx_module/ssfx_rain_module/ssfx_rain_main/splash_alpha_mcm = 0.2
        ssfx_module/ssfx_rain_module/ssfx_rain_main/splash_refraction_mcm = 3
        ssfx_module/ssfx_rain_module/ssfx_rain_main/width_mcm = 0.03
        ssfx_module/ssfx_wetness/ssfx_gloss/auto_gloss_max_mcm = 0.85
        ssfx_module/ssfx_wetness/ssfx_gloss/auto_gloss_mcm = true
        ssfx_module/ssfx_wetness/ssfx_gloss/max_gloss_mcm = 0.9
        ssfx_module/ssfx_wetness/ssfx_gloss/min_gloss_mcm = 0.5
        ssfx_module/ssfx_wetness/ssfx_gloss/specular_color_mcm = 0.6
        ssfx_module/ssfx_wetness/ssfx_gloss/specular_int_mcm = 0.6
        ssfx_module/ssfx_wetness/ssfx_wet_surf/buildup_speed_mcm = 1.5
        ssfx_module/ssfx_wetness/ssfx_wet_surf/cover_distance_mcm = 100
        ssfx_module/ssfx_wetness/ssfx_wet_surf/cover_res_mcm = 1
        ssfx_module/ssfx_wetness/ssfx_wet_surf/dry_speed_mcm = 0.5
        ssfx_module/ssfx_wetness/ssfx_wet_surf/ripples_intensity_mcm = 1.25
        ssfx_module/ssfx_wetness/ssfx_wet_surf/ripples_min_speed_mcm = 0.7
        ssfx_module/ssfx_wetness/ssfx_wet_surf/ripples_size_mcm = 1.5
        ssfx_module/ssfx_wetness/ssfx_wet_surf/ripples_speed_mcm = 1.4
        ssfx_module/ssfx_wetness/ssfx_wet_surf/waterfall_intensity_mcm = 1
        ssfx_module/ssfx_wetness/ssfx_wet_surf/waterfall_min_speed_mcm = 0.2
        ssfx_module/ssfx_wetness/ssfx_wet_surf/waterfall_size_mcm = 1
        ssfx_module/ssfx_wetness/ssfx_wet_surf/waterfall_speed_mcm = 1.5
        ssfx_module/ssr/blur_mcm         = 0.25
        ssfx_module/ssr/general_int_mcm  = 1.15
        ssfx_module/ssr/quality_mcm      = 1
        ssfx_module/ssr/render_scale_mcm = 0.5
        ssfx_module/ssr/sky_int_mcm      = 1.3
        ssfx_module/ssr/use_noise_mcm    = false
        ssfx_module/ssr/weapon_int_max_mcm = 0.05
        ssfx_module/ssr/weapon_int_mcm   = 0.45
        ssfx_module/sss/enable_dir_mcm   = true
        ssfx_module/sss/enable_point_mcm = true
        ssfx_module/sss/len_dir_mcm      = 1
        ssfx_module/sss/len_point_mcm    = 1
        ssfx_module/sss/quality_dir_mcm  = 12
        ssfx_module/sss/quality_point_mcm = 4
        ssfx_module/terrain/distance_mcm = 8
        ssfx_module/terrain/grass_align_mcm = true
        ssfx_module/terrain/grass_slope_mcm = 90
        ssfx_module/terrain/pom_height_mcm = 0.04
        ssfx_module/terrain/pom_quality_mcm = 12
        ssfx_module/terrain/pom_range_mcm = 20
        ssfx_module/terrain/pom_refine_mcm = false
        ssfx_module/terrain/pom_water_level_mcm = 1
        ssfx_module/water/blur_mcm       = 0.5
        ssfx_module/water/blur_pattern_mcm = 1
        ssfx_module/water/caustics_int_mcm = 1
        ssfx_module/water/distortion_mcm = 2
        ssfx_module/water/parallax_height_mcm = 0.05
        ssfx_module/water/parallax_quality_mcm = 1
        ssfx_module/water/reflection_int_mcm = 0.86
        ssfx_module/water/ripples_int_mcm = 0.5
        ssfx_module/water/softborder_mcm = 0.3
        ssfx_module/water/specular_int_mcm = 1
        ssfx_module/water/ssr_quality_mcm = 1
        ssfx_module/water/ssr_res_mcm    = 0.5
        ssfx_module/water/turbidity_mcm  = 0.3
        ssfx_module/wind/grass_push_mcm  = 1.6
        ssfx_module/wind/grass_speed_mcm = 9.7
        ssfx_module/wind/grass_turbulence_mcm = 1.5
        ssfx_module/wind/grass_wave_mcm  = 0.5
        ssfx_module/wind/min_speed_mcm   = 0.1
        ssfx_module/wind/trees_bend_mcm  = 0.9
        ssfx_module/wind/trees_speed_mcm = 9.1
        ssfx_module/wind/trees_trunk_mcm = 0.17
        ssfx_module/wpn_dof/aim_blur_mcm = 2
        ssfx_module/wpn_dof/aim_edgeblur_mcm = 1
        ssfx_module/wpn_dof/aim_fadelen_mcm = 0.25
        ssfx_module/wpn_dof/aim_fadestart_mcm = 0
        ssfx_module/wpn_dof/blur_mcm     = 1.1
        ssfx_module/wpn_dof/edgeblur_mcm = 0.3
        ssfx_module/wpn_dof/fadelen_mcm  = 0.25
        ssfx_module/wpn_dof/fadestart_mcm = 0.15
        ssfx_module/wpn_dof/fdda_mcm     = false
        ssfx_module/wpn_dof/inventory_mcm = true
        ssfx_module/wpn_dof/looting_mutant_mcm = false
        ssfx_module/wpn_dof/pda_mcm      = true
        ssfx_module/wpn_dof/reloading_mcm = false
"""
mgp = {

    "intro": """
**Miracle Graphics Pack** is a pack designed to give the Zone a **realistic**, yet **cinematic look**, with **high-resolution textures**, **improved shaders**, **modern visual effects**, and **custom-made weathers**.

It also features various **atmospheric presets** to make the game **look** and **feel** the way you want it, as well as a **minimalistic** ReShade preset that makes subtle, but significant improvements on the visuals, without much of an impact on performance.
""",
    
    "instp1": """
You will also need **7Zip** for this installation (do not use WinRAR, as it can lead to issues). You can download it here if you don't have it: https://www.7zip.com/

I'd also recommend using it with **Anomaly Mod Configuration Menu**, which you can download here: https://www.moddb.com/mods/stalker-anomaly/addons/anomaly-mod-configuration-menu

**Download these files using the links below - they will be installed through MO2 (choose *ONE* Base Shaders file based on whether you are running Winter, or not):**

***Miracle Graphics Pack (ModDB: ~25GB packed; up to ~40GB unpacked)***: https://www.moddb.com/mods/stalker-anomaly/addons/miracle-graphics-pack

***X-Ray Monolith Modified Exes (GitHub: ~72MB packed; ~196MB unpacked)***: https://github.com/themrdemonized/xray-monolith/releases/download/2025.9.19/STALKER-Anomaly-modded-exes_2025.9.19.zip

***Base Shaders - Regular (Google Drive: ~130MB packed; ~250MB unpacked)***: https://drive.google.com/uc?export=download&id=1W48Dexb3yHj6YMb6wT5WJ8cDciXSCgOW

***Base Shaders - Winter (Google Drive: ~130MB packed; ~250MB unpacked)***: https://drive.google.com/uc?export=download&id=1KA-cwl15vUvpLltuBzGOqg5oWEx5Xxvq

***Atmospherics GAMMA (ModDB: File size changes with updates)***: https://www.moddb.com/mods/stalker-anomaly/addons/hippos-shaders-and-atmospherics

***RESHADE 6.3.3 DX11 (Google Drive: ~115MB packed; ~240MB unpacked)***: https://drive.google.com/uc?export=download&id=1PWpfTfCQYEWr9GsKe0k5X6emepEdT-Rq

If you want the full pack, head to the **STALKER RTac** page to check it out; you won't need the instructions on this page if you are using it. If you only want the graphics pack, follow the instructions here to install it.
""",

    "instp2": """
Open the modified exes file **with 7Zip** and **extract ALL the files into your Anomaly folder**. Once they're extracted (or as they're extracting), go into your `gamedata` folder, and **delete ALL of the folders** in there (if there are any), **EXCEPT** for the `configs` folder.

Then, open the `configs` folder and **delete ALL the files and folders** in there **EXCEPT** for `localization.ltx`, `cache_dbg.ltx` and `axr_options.ltx`(if they are not there, **that's okay**, but **do not delete them if they are there**).

---

**Before you install the remaining files**, you will need to disable **ALL** of your **graphics** mods in MO2. If you want to use any textures **on top of Miracle Graphics Pack**, you can; just place them **underneath** all of these files **after they are installed**.

This includes **Screen Space Shaders, Enhanced Shaders and Color Grading, Beef's NVGs (or any other NVG shader mods), Atmospherics, any **weather** mods (like **Weather Expansion** or **Melancholy Weathers**), and any **texture packs** (like **Ayden's Grass**, **C-Consciousness Grass**, **ATO** or **Rotten Life**).**

Once those are disabled, **install all the files in the order above through MO2**, at the bottom of your modlist. Because of the size of **MGP**, MO2 may **freeze** during the installation; just wait for a bit for the mod to be installed and MO2 will be functional again.

Make sure to select **all** options when installing **Miracle Graphics Pack** (excluding Main Textures, Re.Pack Textures and Cinematic VFX if you want some extra performance), and **select the options below for Atmospherics**:
""",

    "conclusion": """
Once everything is installed, enable these mods, go to your `Anomaly/appdata/` folder, and **delete** the `shaders_cache` folder **if it hasn't been deleted already**.

Finally, run the game **through the Anomaly Launcher** and type `cfg_load [preset]` into the game console to load the atmospheric settings; the "default" preset is `realistic`, but you can choose from **any** of the available presets, which can be viewed on both the **main pack installer** and the `# atmospheric-presets-preview` channel on the official **STALKER RTac** Discord server.
"""
}
rtac = {
    "intro": """---
**STALKER RTac** is a modpack designed around making STALKER Anomaly as realistic as possible, featuring a Cold System, constant psy drain, modified item effects, a realistic body health system, HUD changes, reanimations, and so much more.

If you haven't already, go ahead and join the **STALKER RTac Discord Server** at ***https://discord.gg/mAEhFkyfTj***, to get tech support, update notifications, announcements and other information and support regarding the modpack.

---""",

    "reqsfiles": """---
**STALKER RTac** runs on **STALKER Anomaly**, which is a **standalone mod** for many games in the **STALKER series**. **You will need this to run RTac**.

You will also need **7Zip** for this installation (do not use WinRAR, as it can lead to issues). You can download it here if you don't have it: https://www.7zip.com/

Along with that, you will need some other files. **You will not need to reinstall STALKER Anomaly if you already have version 1.5.3**. To extract files during this installation, **open the archive with 7Zip, highlight the files inside, and drag them to your target location**. Here are links to **all** of the files that you will need for the installation:

***STALKER RTac (~25GB packed; ~95GB unpacked)***: https://www.moddb.com/mods/stalker-anomaly/addons/stalker-real-tactical

***STALKER Anomaly 1.5.3 (ModDB: ~9GB packed; ~15GB unpacked)***: https://www.moddb.com/mods/stalker-anomaly/downloads/stalker-anomaly-153

***Atmospherics GAMMA (ModDB: File size changes with updates)***: https://www.moddb.com/mods/stalker-anomaly/addons/hippos-shaders-and-atmospherics

***Miracle Graphics Pack (ModDB: ~25GB packed; up to ~40GB unpacked)***: https://www.moddb.com/mods/stalker-anomaly/addons/miracle-graphics-pack

***Arrival Anomalies - S.e.m.i.t.o.n.e. (ModDB: File size changes with updates)***: https://www.moddb.com/mods/stalker-anomaly/addons/arrival-anomalies

***Anomaly Mod Configuration Menu - RavenAscendant (ModDB: File size changes with updates)***: https://www.moddb.com/mods/stalker-anomaly/addons/anomaly-mod-configuration-menu

The **final installation size** comes out to **~140GB**, though I'd recommend clearing out **200GB** in advance to avoid any issues with installation.

---""",

    "instp1": """---
To install Anomaly, go to your **base drive** (go to `This PC` in **File Explorer**, and select your drive - preferably your **`C:` drive**; you may have issues otherwise. Then, create a folder for **STALKER Anomaly** (I **highly recommend** to name it `Anomaly` to **avoid file path length issues**).

After that, open the **STALKER Anomaly** file using **7Zip**, select **ALL** the files inside and **drag them into your `Anomaly` folder**.

Once it's done extracting, run `AnomalyLauncher.exe`, select your preferred options, and run the game. Once the main menu appears, **close the game**. This will generate files that **Anomaly will need to run properly**.
""",

    "instp2": """---
From there, create another folder **on your base drive**, and name it `RTac`.

Then, **extract ALL the contents** of the `STALKER RTac.7z` file to your `RTac` folder.

Once that's done, **open MO2** by running `ModOrganizer.exe` (which is inside of your `RTac` folder). Next, install **Atmospherics GAMMA** with the settings in the screenshot below, followed by **Miracle Graphics Pack** into the **RTac Graphics** separator.

To do this, right-click on the **RTac Graphics** separator, hover over `All Mods` and click `Install mod inside...`. Select each file once prompted, and install it, selecting the options in the screenshot below for **Atmospherics**, and all available options for **Miracle Graphics Pack** (except for ATO 5 Ground Textures if you are using Winter - if you want some better performance, you can skip the Main Textures, Re.Pack Textures and Cinematic VFX, though I'd highly recommend getting them). **Ensure to install Atmospherics first, followed by Miracle Graphics Pack**. Once that's done, enable them by clicking on the checkbox to the left of each one.
""",

    "instp3": """
**:red[IMPORTANT:]** If you are using **Winter** or **Early Winter**, make sure you **disable** `(S) Screen Space Shaders 23.5 - Ascii1457`, and **enable** `(S) Screen Space Shaders 23.5 (WINTER) - Ascii1457` instead.
""",

    "instp4": """
Next, expand the **RTac Visuals & Actor Animations** separator by clicking on the arrow to the left of its name. If the arrow is pointing down, the separator has been expanded. Right-click the **first (top) mod** under the **RTac Visuals & Actor Animations** separator, hover over `All Mods`, and click `Install mod above...`. Then, **install Arrival Anomalies** with your preferred settings, and **enable** it by clicking the checkbox on the **left** side of the screen. Your **load order** should look like the image below:
""",

    "instp5": """
Once Arrival is installed, expand the **RTac HUD** separator. Right-click the **first (top) mod** under the **RTac HUD** separator, hover over `All Mods`, and click `Install mod above...`. Then, **install Anomaly Mod Configuration Menu**, and **enable** it. Your load order should look like the image below:
""",

    "conclusion": """---
Finally, go to your `Anomaly/appdata/` folder, and **delete** the `shaders_cache` folder **if it's there**. If it isn't, **don't worry** - it's not an issue.

Now, you can play **STALKER RTac**. Launch the game **using the Anomaly Launcher**, and **enjoy the game**! Once the game loads up, open the console and type `cfg_load [preset]` into the game console to load the atmospheric settings; the "default" preset is `realistic`, but you can choose from any of the available presets, which can be viewed on both the **main pack installer** and the `# atmospheric-presets-preview` channel on the official **STALKER RTac** Discord server.

I also recommend getting my recommended settings to ensure everything works properly, by following the instructions on the `# recommended-settings` channel.

You can load any preset you like. The format for this command `cfg_load [preset]`; instead of `[preset]`, use any of the presets in the `# atmospheric-presets-preview` channel.

If you would like my `user.ltx` (game settings) file, ping me and ask for it in the `# tech-support` channel, and I'll send it to you when I can.

If you are confused, or have any issues, please check the `# common-fixes-and-tips` channel on the **STALKER RTac Discord Server** for anything that could help. If you cannot find anything to solve your issue, **contact me** on the `# tech-support` channel, and I will help you however I can.

Also, if you have any feedback, please let me know in the `# feedback` channel, and I will take a look at it as soon as I can.
"""
}
graphicslist = {

    "base shaders": """
- **Enhanced Shaders & Colour Grading 1.10 - KennShade:** Overhauls the shaders and visual effects, as well as post-processing and lighting for better visual fidelity and customizability.

- **Beef's NVGs Improved 1.3 - party_50:** An improved version of Beef's NVGs, featuring better animations, compatibility and quality of life.

- **Screen Space Shaders - Ascii1457:** Implements modern shader methods, adding ambient occlusion, screen space (and volumetric) lighting and reflections, improved water effects and depth of field, as well as various post-processing effects, such as TAA, bloom and lens flare.
    """,

    "shaders": """
- **Shaders Look Better (Motion Blur & Shaders Improvements):** Makes improvements to shaders and performance, and refines motion blur to look smoother and more realistic.

- **Dark Signal Weather and Ambiance Audio - Shrike:** G.A.M.M.A.'s version of this mod, included for compatibility purposes.

- **HollywoodFX V3.1.5:** Adds cinematic VFX for gunshots, explosions, and other effects, as well as better sounds for them.
    """,

    "textures": """
- **Anomaly Texture Overhaul 5 - PAUL_8558:** A complete texture overhaul that adds detailed 4K and 8K textures, which add to the depressing realism and immersion of the game.

- **Re.Pack Texture Pack Series - Hades@DK:** Adds high-res textures - ranging from 4K to 16K - to many different surfaces around the Zone. It includes high-res textures for glass, barbed wire, pseudodogs, lurkers, doors, and so much more.
    """,

    "mask textures": """
- **Grok's Masks and Reflections 2.1.0:** Redone mask lighting effects with reflections and refractions, using blurred versions of Nav's 4K Mask Textures.

- **Drunk's 4K Mask Textures:** Adds realistic 4K mask textures, complete with droplets and a somewhat blurred overlay.
    """,

    "maps": """
- **Re.Pack PDA Package V1.3**: Adds 16K PDA maps that add even more detail and zooming capability to your PDA.
    """,

    "luts": """
- **Atmospherics Pre-SSS 22 LUTs:** Realistic, neutral LUTs from Atmospherics before the Screen Space Shaders 22 update. Courtesy of Shahryar.
""",

    "seasonal": """
- **Graupel's Winter Mod v1.0.2:** A mod that turns the Zone into a bright Winter wonderland, or an accurate representation of the early stages of Winter.

- **Aydin's Grass Tweaks 4.0:** A recolored version of the Golden Autumn Retexture mod, made to fit different seasons.

- **Re\:Pack Foliage Package 1.2:** Adds 16K textures to leaves.

- **C-Consciousness Grass Overhaul v0.55:** Adds 8K foliage, with recolors and resizing to fit each season. Made by **Huh?**, with help from **Hoddminir** and poppy textures from **https://pngimg.com**.

- **Rotten Life Ground Textures:** Adds 4K realistic terrain textures, available in Summer, Fall and Late Fall.
    """,

    "summer": """
- **Aydin's Grass Tweaks 4.0**

- **Re\:Pack Foliage Package**

- **C-Consciousness Grass Overhaul v0.55**

- **Rotten Life Ground Textures**

- **ATO 5 Foliage Textures (Trees & Bushes - not grass)**
    """,

    "late fall": """
- **Aydin's Grass Tweaks 4.0**

- **Re\:Pack Foliage Package**

- **C-Consciousness Grass Overhaul v0.55**

- **Rotten Life Ground Textures**
    """,

    "early winter": """
- **Graupel's Winter Mod v1.0.2**

- **Aydin's Grass Tweaks 4.0**

- **Re.Pack Foliage Package**

- **C-Consciousness Grass Overhaul v0.55**
    """,

    "winter": """
- **Graupel's Winter Mod v1.0.2**
    """,

    "weather": """
- **Weather Expansion For Atmospherics - Ani HVX:** Adds a wide variety of weathers to the game, all of which look realistic, yet cinematic.

- **Apocalyptic Blowout Overhaul 4.0.1:** Revamps blowouts to look incredibly beautiful.

- **Awesomedude's Weather Edits For Weather Expansion:** My own edits to the weathers, adjusting and reworking the weather for cinematic sunrises and sunsets, moderately bright days, dark and forboding nights, aggressive, yet beautiful storms and menacing, but less suffocating fog.
    """,

    "luts": """
- **Atmospherics Pre-SSS 22 LUTs:** Realistic, neutral LUTs from Atmospherics before the Screen Space Shaders 22 update. Courtesy of Shahryar.
"""

}
screenshots = [
    "Army Warehouses Sunset",
    "Freedom Base Sunrise (Window)",
    "Freedom Base Sunset",
    "Freedom Base Campfires in The Rain",
    "Driving in Dead City",
    "Night in Red Forest",
    "Great Swamps Rain",
    "Cordon Sunset",
    "Winter Wonderland",
    "Yantar Mobile Laboratory",
]

if page == "STALKER RTac":

    st.title("Homepage")

    st.write(rtac['intro'])

    st.header("Requirements/Pre-Installation")
    st.write(rtac['reqsfiles'])

    st.header("STALKER RTac Installation")

    st.write(rtac['instp1'])
    st.write(rtac['instp2'])
    st.image("AtmosOptions.png")
    st.write(rtac['instp3'])
    st.subheader("Graphics Load Order:")
    st.image("GraphicsLoadOrder.png")
    st.subheader("Installing Arrival Anomalies:")
    st.write(rtac['instp4'])
    st.image("ArrivalLoadOrder.png")
    st.subheader("Installing Anomaly Mod Configuration Menu:")
    st.write(rtac['instp5'])
    st.image("MCMLoadOrder.png")
    
    st.write(rtac['conclusion'])

elif page == "Miracle Graphics Pack":

    st.title("Miracle Graphics Pack")
    st.write("---")
    st.write(mgp["intro"])


    previewscreenshots = st.checkbox("**Load Preview Screenshots**", value=False)

    if previewscreenshots:

        with st.expander("**Preview Screenshots**"):

            st.header("Preview Screenshots:")
            st.write("**Note:** These screenshots were taken on a **laptop** with 16GB of RAM, a 1TB SSD, an 11th-gen i7 and an RTX 3060.")

            showScreenshots(screenshots, ".png")

    st.write("---")
    st.subheader("Installation:")
    st.write(mgp["instp1"])
    st.write("---")
    st.write(mgp["instp2"])
    st.image("AtmosOptions.png")
    st.write("---")
    st.write(mgp["conclusion"])

    st.write("---")

    st.header("Mods Included In Miracle Graphics Pack:")

    st.subheader("Base Shaders:")
    st.write(graphicslist["base shaders"])

    st.subheader("Shaders & VFX:")
    st.write(graphicslist["shaders"])

    st.subheader("Texture Packs:")
    st.write(graphicslist["textures"])

    st.subheader("RTac Weather:")
    st.write(graphicslist["weather"]) 

    st.subheader("Mask Textures:")
    st.write(graphicslist["mask textures"])

    st.subheader("16K PDA Maps:")
    st.write(graphicslist["maps"])
    
    st.subheader("Miracle LUTs:")
    st.write(graphicslist["luts"])

    st.subheader("Seasonal Mods:")
    st.write(graphicslist["seasonal"])

    st.subheader("Summer/Autumn:")
    st.write(graphicslist["summer"])

    st.subheader("Late Fall:")
    st.write(graphicslist["late fall"])

    st.subheader("Early Winter:")
    st.write(graphicslist["early winter"])

    st.subheader("Winter:")
    st.write(graphicslist["winter"])

elif page == "MCM Settings For SSS":

    st.write("This will edit your MCM settings file to change its settings to what they should be for this pack.")
    st.write("Upload your `axr_options.ltx` file from your G.A.M.M.A. MCM values mod in MO2 - to get it, open MO2, search for `G.A.M.M.A. MCM values`, right-click on the mod and hit `Reveal in Explorer`.")
    st.write("After that, in the file explorer window that pops up, open the `gamedata` folder, open the `configs` folder inside of that, and drag and drop the `axr_options.ltx` file onto the website.")
    st.write("Then, download the converted file, drag it into the `configs` folder and replace the existing file when prompted.")

    userfile = st.file_uploader("")

    if userfile != None:

        if userfile.name != "axr_options.ltx":
            st.subheader("This is not a valid MCM values file. Please use a valid file.")

        else:

            strio = StringIO(userfile.getvalue().decode("utf-8"))
            userout = strio.read() + sssmcm
            download = st.download_button("Download Converted File", data=userout, file_name="axr_options.ltx")

elif page == "ReShade File Finder":

    st.write("This page will give you the path to your ReShade file. Just enter the information below (highlight a folder in File Explorer and use `Ctrl+Shift+C` to copy its path), and hit **Locate**. Then, the path of the ReShade presets folder will show below. Copy it and paste it in the ReShade menu, and select the ReShade preset that you want.")

    gammapath = st.text_input("Enter the file path of your **RTac/GAMMA** folder:")
    rename = st.checkbox("Did you rename the **Miracle Graphics Pack** mod?")
    name = "Miracle Graphics Pack"
    separator = "/"

    if gammapath != "":

        if rename:
            name = st.text_input("What did you rename it to?")

        if gammapath[2] == "\\":
            separator = "\\"

        if gammapath[-1] == separator:
            gammapath = gammapath[:-1]

        if st.button("Locate"):
            st.write(f"**Preset Folder Path: `{gammapath}{separator}mods{separator}{name}{separator}bin{separator}`**")

elif page == "Atmospheric Preset Editor":

    st.write("This page will allow you to create your **own** atmospheric preset.")
    st.write("On the sidebar to the left, select the settings that you want to add to your preset. Then, fill out the fields that appear below.")

    preset = ""
    settings = {}

    with st.sidebar.expander("**Settings**"):

        startfrom = st.radio("**How do you want to start creating your preset?**", ["Start From Scratch", "Start From a Miracle Graphics Preset", "Start From an Existing Preset"])

        if startfrom == "Start From a Miracle Graphics Preset":
            atmospreset = atmospresets[st.radio("**Select a Preset to Start From:**", atmospresetlist)]

        elif startfrom == "Start From an Existing Preset":

            existingpreset = st.file_uploader("**Upload your preset here:**")

            if existingpreset != None:

                if existingpreset.name[-4:] == ".ltx":
                    strio = StringIO(existingpreset.getvalue().decode("utf-8"))
                    preset = strio.read()+"\n\n\n"

                else:
                    st.write("This is not a valid preset. Make sure to upload one that has a \"`.ltx`\" file extension - they can be found in the `appdata` folder in a mod, or the base `Anomaly` folder.")

        st.header("Preset Settings")

        selectall = st.checkbox("Select All", True)

        st.subheader("Main Shader Settings")

        selectallss = st.checkbox("Select All Shader Settings", selectall)
        shader1 = st.checkbox("Bright Colors", selectallss)
        shader2 = st.checkbox("Dark Colors", selectallss)
        shader3 = st.checkbox("Shader Gamma (mid-range colors)", selectallss)
        shader4 = st.checkbox("Contrast", selectallss)

        st.subheader("Post-Processing")

        selectallpp = st.checkbox("Select All Post-Process Settings", selectall)
        exposure = st.checkbox("Camera Exposure", selectallpp)
        gamma = st.checkbox("Display Gamma", selectallpp)
        saturation = st.checkbox("Color Saturation/Strength", selectallpp)
        cgrading = st.checkbox("Color Grading", selectallpp)

        st.subheader("Grass Settings")

        selectallgs = st.checkbox("Select All Grass Settings", selectall)
        grassheight = st.checkbox("Grass Size", selectallgs)
        grassdensity = st.checkbox("Grass Density", selectallgs)
        grassrender = st.checkbox("Grass Render Distance", selectallgs)

        st.subheader("Advanced Options")

        selectallao = st.checkbox("Select All Advanced Options", selectall)
        mblur = st.checkbox("Motion Blur Intensity", selectallao)
        sunlum = st.checkbox("Sun Brightness", selectallao)
        sunlumamb = st.checkbox("Ambient Sunlight Brightness", selectallao)
        tonemapamt = st.checkbox("Tonemapping Amount", selectallao)
        tonemapadapt = st.checkbox("Tonemapping Adaptation", selectallao)

        st.subheader("Screen Space FX Settings")

        selectallssfx = st.checkbox("Select All SSFX Settings", selectall)
        hudhemi = st.checkbox("Additional HUD Brightness", selectallssfx)

    if exposure or gamma or saturation or cgrading:

        st.write("---")
        st.header("Post-Processing")

        cols = st.columns(3)

        colindex = 0

        if exposure:
            settings['r__exposure'] = cols[colindex].slider("**Camera Exposure (`r__exposure`)**", min_value=0.5, max_value=4.0, value=1.0, step=0.01)
            colindex += 1

        if gamma:
            settings['r__gamma'] = cols[colindex].slider("**Display Gamma (`r__gamma`)**", min_value=0.5, max_value=2.2, value=1.0, step=0.01)
            colindex += 1

        if saturation:
            settings['r__saturation'] = cols[colindex].slider("**Color Saturation (`r__saturation`)**", min_value=0.0, max_value=2.0, value=1.0, step=0.01)

        st.header("")
        st.subheader("**Color Grading**")
        st.write("**(`r__color_grading`)**")

        cols = st.columns(3)

        if cgrading:
            settings["r__color_grading"] = [cols[0].number_input("**Red**", min_value=0.0, max_value=1.0, value=0.0, step=0.01), cols[1].number_input("**Green**", min_value=0.0, max_value=1.0, value=0.0, step=0.01), cols[2].number_input("**Blue**", min_value=0.0, max_value=1.0, value=0.0, step=0.01)]

    if grassheight or grassdensity or grassrender:

        st.write("---")
        st.header("Grass Settings (SAVE RELOAD REQUIRED)")

        cols = st.columns(3)

        colindex = 0

        if grassheight:
            settings['r__detail_height'] = cols[colindex].slider("**Grass Size (`r__detail_height`)**", min_value=0.5, max_value=2.0, value=0.8, step=0.01)
            colindex += 1

        if grassdensity:
            settings['r__detail_density'] = 1 - ( cols[colindex].slider("**Grass Density (`r__detail_density`)**", min_value=0.0, max_value=1.0, value=0.5, step=0.01) * (0.96) )
            colindex += 1

        if grassrender:
            settings['r__detail_radius'] = cols[colindex].slider("**Grass Render Distance (`r__detail_radius`)**", min_value=0, max_value=250, value=150, step=5)


    if sunlum or sunlumamb or tonemapamt or tonemapadapt:

        st.write("---")
        st.header("Advanced Options")

        if mblur:
            mblurintensity = st.slider("**Motion Blur Intensity (set to 0 to turn off) (`r2_mblur_enabled` & `r2_mblur`)**", min_value=0.0, max_value=1.0, value=0.0, step=0.01)

            if mblurintensity == 0:
                settings["r2_mblur_enabled"] = "off"
            else:
                settings["r2_mblur_enabled"] = "on"

            settings['r2_mblur'] = mblurintensity

        if sunlum:
            settings['r2_sun_lumscale'] = st.slider("**Sun Brightness (`r2_sun_lumscale`)**", min_value=-1.0, max_value=3.0, value=3.0, step=0.01)

        if sunlumamb:
            settings['r2_sun_lumscale_amb'] = st.slider("**Ambient Sunlight Brightness (`r2_sun_lumscale_amb`)**", min_value=0.0, max_value=3.0, value=2.0, step=0.01)

        if tonemapamt:

            tonemapamtinput = st.slider("**Tonemapping Amount - Set to 0 to turn off tonemapping (`r2_tonemap` & `r2_tonemap_amount`)**", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

            if tonemapamtinput == 0:
                settings['r2_tonemap'] = "off"

            else:
                settings['r2_tonemap'] = "on"

            settings['r2_tonemap_amount'] = tonemapamtinput

        if tonemapadapt:
            settings['r2_tonemap_adaptation'] = st.slider("**Tonemapping Adaptation (`r2_sun_lumscale_amb`)**", min_value=0.01, max_value=10.0, value=3.0, step=0.01)

    if hudhemi:

        st.write("---")
        st.header("Screen Space FX Settings")

        settings['ssfx_hud_hemi'] = st.number_input("**Additional HUD Brightness (`ssfx_hud_hemi`)**", min_value=0.0, max_value=1.0, value=0.0, step=0.01)

    if shader1 or shader2 or shader3 or shader4:

        st.write("---")
        st.header("Main Shader Settings")

        cols = st.columns(5)

        cols[0].write("**Setting (Parameter)**")
        cols[1].write("**Red Intensity**")
        cols[2].write("**Green Intensity**")
        cols[3].write("**Blue Intensity**")
        cols[4].write("**Overall Intensity**")

        cols[0].write("")

        if shader1:
            cols[0].write("**Bright Colors (0 to 1)**")
            cols[0].write("**`shader_param_1`**")
            settings['shader_param_1'] = [cols[1].number_input("Red1", min_value=0.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[2].number_input("Green1", min_value=0.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[3].number_input("Blue1", min_value=0.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[4].number_input("**Overall Intensity Offset 1**", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden")]

        if shader2:
            cols[0].write("**Dark Colors (0 to 1)**")
            cols[0].write("**`shader_param_2`**")
            settings['shader_param_2'] = [cols[1].number_input("Red2", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden"), cols[2].number_input("Green2", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden"), cols[3].number_input("Blue2", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden"), cols[4].number_input("**Overall Intensity Offset 2**", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden")]

        if shader3:
            cols[0].write("**Shader Gamma (-1 to 1)**")
            cols[0].write("**`shader_param_3`**")
            settings['shader_param_3'] = [cols[1].number_input("Red3", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[2].number_input("Green3", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[3].number_input("Blue3", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[4].number_input("**Overall Intensity Offset 3**", min_value=0.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden")]

        if shader4:
            cols[0].write("**Contrast (-1 to 1)**")
            cols[0].write("**`shader_param_4`**")
            settings['shader_param_4'] = [cols[1].number_input("Red4", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[2].number_input("Green4", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[3].number_input("Blue4", min_value=-1.0, max_value=1.0, value=1.0, step=0.01, label_visibility="hidden"), cols[4].number_input("**Overall Intensity Offset 4**", min_value=-1.0, max_value=1.0, value=0.0, step=0.01, label_visibility="hidden")]

    for param, val in zip(settings, settings.values()):

        if type(val) == list:

            preset += f"{param} ("

            for v in val:
                if type(v) != str:
                    preset += f"{round(v, 2)}, "
                else:
                    preset += f"{v}, "

            preset = preset[:-2]+")\n"

        else:

            if type(val) != str:
                preset += f"{param} {round(val, 2)}\n"
            else:
                preset += f"{param} {val}\n"


    if preset != None:

        st.header("Final Steps")

        preset = preset.split("\n")

        rnewline = True
        rcgnewline = True
        r2newline = True
        ssfxnewline = True
        shadernewline = True

        for line in range(len(preset)):

            if "r__" in preset[line] and rnewline:
                preset[line] = "\n"+str(preset[line])
                rnewline = False

            if "r__color_grading" in preset[line] and rcgnewline:
                preset[line] = "\n"+str(preset[line])
                rcgnewline = False

            if "r2_" in preset[line] and r2newline:
                preset[line] = "\n"+str(preset[line])
                r2newline = False

            if "ssfx" in preset[line] and ssfxnewline:
                preset[line] = "\n"+str(preset[line])
                ssfxnewline = False

            if "shader_param" in preset[line] and shadernewline:
                preset[line] = "\n"+str(preset[line])
                shadernewline = False

        preset = "\n".join(preset)

        if startfrom == "Start From a Miracle Graphics Preset":
            preset = atmospreset+"\n\n"+preset

        presetname = st.text_input("What do you want to name your preset?", "MyPreset.ltx").strip()

        if presetname[-4:] != ".ltx":
            presetname = presetname + ".ltx"

        with st.expander("**Preset Preview**", expanded=True):

            st.header(presetname)
            st.write(f"```{preset}\n```")

        st.download_button(f"**Download Your Preset (:blue[{presetname}])**", data=preset, file_name=presetname)



import gradio as gr
from pathlib import Path
from modules import script_callbacks, shared
import json
import os

# Webui root path
ROOT_DIR = Path().absolute()


def on_ui_tabs():
    theme = gr.themes.Base(
        primary_hue=gr.themes.Color(primary_100="#e0e7ff", primary_200="#c7d2fe", primary_300="#a5b4fc", primary_400="#818cf8", primary_50="#eef2ff", primary_500="#6366f1", primary_600="#4f46e5", primary_700="#4338ca", primary_800="#3730a3", primary_900="#312e81", primary_950="#1e1b4b"),
        secondary_hue="None",
        neutral_hue=gr.themes.Color(neutral_100="#f1f5f9", neutral_200="#e2e8f0", neutral_300="#cbd5e1", neutral_400="#94a3b8", neutral_50="#f8fafc", neutral_500="#64748b", neutral_600="#475569", neutral_700="#334155", neutral_800="#1e293b", neutral_900="#0f172a", neutral_950="#020617"),
        text_size="text_lg",
        spacing_size="spacing_lg",
        font=['Inter var', 'ui-sans-serif', 'system-ui', '-apple-system'],
        font_mono=[' ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco'],
    ).set(
        body_background_fill='*neutral_50',
        body_background_fill_dark='*neutral_950',
        body_text_color_dark='*primary_50',
        body_text_color_subdued='*neutral_500',
        background_fill_primary='*primary_50',
        color_accent_soft_dark='*primary_500',
        shadow_drop='rgba(0, 0, 0, 0.01) 0 1px 2px',
        shadow_drop_lg='rgba(0, 0, 0, 0.03) 0 20px 13px ',
        shadow_spread_dark='3px',
        block_background_fill_dark='*neutral_900',
        chatbot_code_background_color_dark='*neutral_900',
        checkbox_background_color_dark='*primary_50',
        input_shadow='*shadow_drop',
        button_large_text_size='*text_md',
        button_primary_background_fill='*primary_600',
        button_primary_text_color='White',
        button_secondary_background_fill='*primary_100',
        button_secondary_background_fill_dark='*primary_700',
        button_secondary_text_color='*neutral_800'
    )
    
    with gr.Blocks(theme=theme, analytics_enabled=False) as GPT_Blocks:
        gr.HTML(
            "<p id='change',style=\"margin-bottom:0.75em\">This is a test.Designed by yuki</p>")
        with gr.Row():
            with gr.Column(scale=45):
                textbox_info = gr.Textbox(label='Something else', value=f'Holy shit',
                                          readonly=True, elem_id="shit_one")
            auto_trans_btn = gr.Button(value="Press to start", variant='primary', elem_id="auto_trans_btn")
            with gr.Column(scale=80):
                change_btn = gr.Button(value="change", variant='primary', elem_id="change_btn")

    return [(GPT_Blocks, "GPT-Lu", "GPT-Lu")]


script_callbacks.on_ui_tabs(on_ui_tabs)
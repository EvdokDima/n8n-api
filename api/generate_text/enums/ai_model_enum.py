from enum import Enum

class AIModel(str, Enum):
    # OpenAI
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_4 = "gpt-4"
    GPT_4O = "gpt-4o"
    GPT_4O_MINI = "gpt-4o-mini"
    O1 = "o1"
    O1_MINI = "o1-mini"
    O3_MINI = "o3-mini"

    # GigaChat
    GIGACHAT = "gigachat"

    # Meta
    META_AI = "meta-ai"

    # Meta Llama
    LLAMA_2_7B = "llama-2-7b"
    LLAMA_3_8B = "llama-3-8b"
    LLAMA_3_70B = "llama-3-70b"
    LLAMA_3_1_8B = "llama-3.1-8b"
    LLAMA_3_1_70B = "llama-3.1-70b"
    LLAMA_3_1_405B = "llama-3.1-405b"
    LLAMA_3_2_1B = "llama-3.2-1b"
    LLAMA_3_2_3B = "llama-3.2-3b"
    LLAMA_3_2_11B = "llama-3.2-11b"
    LLAMA_3_2_90B = "llama-3.2-90b"
    LLAMA_3_3_70B = "llama-3.3-70b"

    # Mistral
    MIXTRAL_8X7B = "mixtral-8x7b"
    MIXTRAL_8X22B = "mixtral-8x22b"
    MISTRAL_NEMO = "mistral-nemo"
    MIXTRAL_SMALL_24B = "mixtral-small-24b"

    # NousResearch
    HERMES_3 = "hermes-3"

    # Microsoft
    PHI_3_5_MINI = "phi-3.5-mini"
    PHI_4 = "phi-4"
    WIZARDLM_2_7B = "wizardlm-2-7b"
    WIZARDLM_2_8X22B = "wizardlm-2-8x22b"

    # Google DeepMind
    GEMINI_EXP = "gemini-exp"
    GEMINI_1_5_FLASH = "gemini-1.5-flash"
    GEMINI_1_5_PRO = "gemini-1.5-pro"
    GEMINI_2_0 = "gemini-2.0"
    GEMINI_2_0_FLASH = "gemini-2.0-flash"
    GEMINI_2_0_FLASH_THINKING = "gemini-2.0-flash-thinking"
    GEMINI_2_0_PRO = "gemini-2.0-pro"

    # Anthropic
    CLAUDE_3_HAIKU = "claude-3-haiku"
    CLAUDE_3_SONNET = "claude-3-sonnet"
    CLAUDE_3_OPUS = "claude-3-opus"
    CLAUDE_3_5_SONNET = "claude-3.5-sonnet"
    CLAUDE_3_7_SONNET = "claude-3.7-sonnet"
    CLAUDE_3_7_SONNET_THINKING = "claude-3.7-sonnet-thinking"

    # Reka AI
    REKA_CORE = "reka-core"

    # Blackbox AI
    BLACKBOXAI = "blackboxai"
    BLACKBOXAI_PRO = "blackboxai-pro"

    # CohereForAI
    COMMAND_R = "command-r"
    COMMAND_R_PLUS = "command-r-plus"
    COMMAND_R7B = "command-r7b"
    COMMAND_A = "command-a"

    # Qwen
    QWEN_1_5_7B = "qwen-1.5-7b"
    QWEN_2_72B = "qwen-2-72b"
    QWEN_2_VL_7B = "qwen-2-vl-7b"
    QWEN_2_5_72B = "qwen-2.5-72b"
    QWEN_2_5_CODER_32B = "qwen-2.5-coder-32b"
    QWEN_2_5_1M = "qwen-2.5-1m"
    QWEN_2_5_MAX = "qwen-2-5-max"
    QWQ_32B = "qwq-32b"
    QVQ_72B = "qvq-72b"

    # Inflection
    PI = "pi"

    # DeepSeek
    DEEPSEEK_CHAT = "deepseek-chat"
    DEEPSEEK_V3 = "deepseek-v3"
    DEEPSEEK_R1 = "deepseek-r1"
    JANUS_PRO_7B = "janus-pro-7b"

    # x.ai
    GROK_3 = "grok-3"
    GROK_3_R1 = "grok-3-r1"

    # Perplexity AI
    SONAR = "sonar"
    SONAR_PRO = "sonar-pro"
    SONAR_REASONING = "sonar-reasoning"
    SONAR_REASONING_PRO = "sonar-reasoning-pro"
    R1_1776 = "r1-1776"

    # Nvidia
    NEMOTRON_70B = "nemotron-70b"

    # Databricks
    DBRX_INSTRUCT = "dbrx-instruct"

    # THUDM
    GLM_4 = "glm-4"

    # MiniMax
    MINI_MAX = "mini_max"

    # 01-ai
    YI_34B = "yi-34b"

    # Cognitive Computations
    DOLPHIN_2_6 = "dolphin-2.6"
    DOLPHIN_2_9 = "dolphin-2.9"

    # DeepInfra
    AIROBOROS_70B = "airoboros-70b"

    # Lizpreciatior
    LZLV_70B = "lzlv-70b"

    # OpenBMB
    MINICPM_2_5 = "minicpm-2.5"

    # Ai2
    TULU_3_1_8B = "tulu-3-1-8b"
    TULU_3_70B = "tulu-3-70b"
    TULU_3_405B = "tulu-3-405b"
    OLMO_1_7B = "olmo-1-7b"
    OLMO_2_13B = "olmo-2-13b"
    OLMO_2_32B = "olmo-2-32b"
    OLMO_4_SYNTHETIC = "olmo-4-synthetic"

    # Liquid AI
    LFM_40B = "lfm-40b"

    # Evil
    EVIL = "evil"

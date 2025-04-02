import os
import datetime
from google import genai
from google.genai import types
import markdown
import re

# Initialize the Google Generative AI client
client = genai.Client(api_key="AIzaSyCzvinODVQUtFGrxCNh1bSTRvx1_0muRVQ")

def generate_linkedin_post(blog_url, blog_title, video_url, blog_content, output_folder="linkedin_posts"):
    """Generate a LinkedIn post to promote the Medium blog article based on the YouTube video content"""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Prompt engineered for LinkedIn post creation
    prompt = f"""
    Create a compelling LinkedIn post that I can use to share my Medium blog article with my professional network.
    
    Blog Title: {blog_title}
    Blog URL: {blog_url}
    Original YouTube Video: {video_url}
    
    Here's the content of my blog (which was based on the YouTube video):
    {blog_content[:2000]}  # Using first 2000 chars to stay within token limits
    
    The LinkedIn post should:
    1. Sound authentic and personal, as if I wrote it myself after publishing my blog
    2. Directly reference the ACTUAL CONTENT and TOPIC from the YouTube video/blog
    3. Briefly highlight 2-3 key insights or points from the actual video/blog content
    4. Include a personal touch about why I found this topic interesting or important
    5. Have a friendly call-to-action inviting connections to read the full article, give it a clap if they enjoy it
    6. Include 3-4 relevant hashtags that relate to the specific topic of the video/blog
    7. Be conversational and engaging, avoiding overly promotional language
    8. Be between 150-250 words with appropriate spacing for LinkedIn readability
    
    IMPORTANT: The post should promote the actual content and insights from the YouTube video that I've written about in my blog. DO NOT focus on the process of converting YouTube to blogs.
    
    The tone should be professional but warm, as if I'm sharing my work with colleagues and connections who would find value in it.
    """
    
    print("Generating LinkedIn post...")
    
    # Create the generate content config
    generate_content_config = types.GenerateContentConfig(
        temperature=0.7,  # Slightly higher temperature for creative variation
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-pro-exp-03-25",
        contents=types.Content(parts=[types.Part(text=prompt)]),
        config=generate_content_config,
    )
    
    # Extract video ID for filename
    video_id = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", video_url).group(1)
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    
    # Save the LinkedIn post as text
    filename = f"{output_folder}/{timestamp}_{video_id}_linkedin.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    
    print(f"LinkedIn post generated successfully!")
    print(f"Post saved to: {filename}")
    
    return filename, response.text

def generate_twitter_post(blog_url, blog_title, video_url, blog_content, output_folder="twitter_posts"):
    """Generate a Twitter/X post to promote the Medium blog article based on the YouTube video content"""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Prompt engineered for Twitter/X post creation
    prompt = f"""
    Create an engaging Twitter/X post that I can use to share my Medium blog article.
    
    Blog Title: {blog_title}
    Blog URL: {blog_url}
    Original YouTube Video: {video_url}
    
    Here's the content of my blog (which was based on the YouTube video):
    {blog_content[:1000]}  # Using first 1000 chars to stay within token limits
    
    The Twitter/X post should:
    1. Be concise and impactful (under 280 characters)
    2. Start with a hook or interesting insight directly from the ACTUAL CONTENT of the YouTube video/blog
    3. Sound authentic and personal, as if I wrote it myself
    4. Include 1-2 relevant hashtags related to the specific topic of the video/blog
    5. End with a clear call-to-action to read my article
    6. Be conversational and engaging
    
    IMPORTANT: The post should promote the actual content and insights from the YouTube video that I've written about in my blog. DO NOT focus on the process of converting YouTube to blogs.
    
    The tone should be informative yet casual, perfect for Twitter's fast-paced environment.
    """
    
    print("Generating Twitter/X post...")
    
    # Create the generate content config
    generate_content_config = types.GenerateContentConfig(
        temperature=0.7,  # Slightly higher temperature for creative variation
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-pro-exp-03-25",
        contents=types.Content(parts=[types.Part(text=prompt)]),
        config=generate_content_config,
    )
    
    # Extract video ID for filename
    video_id = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", video_url).group(1)
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    
    # Save the Twitter post as text
    filename = f"{output_folder}/{timestamp}_{video_id}_twitter.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    
    print(f"Twitter/X post generated successfully!")
    print(f"Post saved to: {filename}")
    
    return filename, response.text

def generate_medium_blog(youtube_url, output_folder="blogs"):
    """Generate a Medium-optimized blog post from a YouTube video"""
    
    # Create output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Prompt engineered for Medium blog creation
    prompt = """
    You are a world-class content creator with deep expertise in digital content strategy, SEO optimization, and the Medium platform. Your task is to transform the YouTube video content into an exceptional Medium blog post that achieves three critical goals: 1) ranks highly in search engines, 2) performs exceptionally well on Medium's internal algorithms, and 3) provides genuine value to readers while maintaining an authentic human voice.
        CONTENT EXTRACTION FRAMEWORK
        Begin by analyzing the YouTube video through these specific lenses:

        Core Thesis Identification: What central argument or insight does this video present?
        Knowledge Structure: How does the video build its case? What is the logical progression?
        Evidence Assessment: What data, examples, or case studies support the main claims?
        Unique Perspective: What distinctive viewpoint or approach does the creator offer?
        Audience Alignment: Who is the intended audience and what do they need to understand?
        Search Intent Mapping: What questions would lead someone to seek this information?

        CONTENT ARCHITECTURE
        Strategic Title Construction (75-85 characters)
        Create a title that incorporates:

        A high-value primary keyword in the first half
        An emotional trigger word (discover, proven, essential, surprising, etc.)
        A clear benefit or outcome promise
        A curiosity gap or intriguing element
        Natural language flow that avoids clickbait formulations

        Subtitle Formulation (100-120 characters)
        Develop a subtitle that:

        Complements rather than repeats the title's message
        Incorporates secondary keywords
        Establishes your authority perspective
        Hints at the depth of insights to follow

        Introduction Sequence (300-400 words)
        Craft an opening that follows this psychological pattern:

        Pattern Interrupt: Begin with an unexpected statement, counterintuitive observation, or provocative question that challenges conventional thinking on the topic.
        Relevance Bridge: Connect the pattern interrupt directly to the reader's current situation or pain point within 2-3 sentences.
        Authority Foundation: Subtly establish credibility through demonstrated knowledge or perspective (not claimed expertise).
        Narrative Setup: Frame the content as a journey of discovery or transformation.
        Benefit Articulation: Explicitly state what the reader will gain, learn, or be able to do after reading.
        Transition Mechanism: Create a natural segue into the main content that builds anticipation.

        Content Body Architecture
        Structure the main content in one of these proven frameworks (select the most appropriate):

        Transformation Framework: Before state → Process → After state
        Problem-Solution Chain: Problem definition → Failed approaches → Optimal solution → Implementation
        Expertise Escalator: Beginner insights → Intermediate concepts → Advanced strategies
        Perspective Contrast: Common view → Limitations → Alternative approach → Comparative benefits

        Within your chosen framework:

        Create 4-6 main sections with H2 headings that:

        Include semantically relevant keywords
        Promise specific value in each section
        Follow a logical progression
        Create a complete narrative arc


        For each main section:

        Begin with a mini-hook that justifies the section's importance
        Present the core concept or argument clearly
        Support with evidence from the video (data, examples, demonstrations)
        Add unique analysis that goes beyond the video's explicit content
        Include a real-world application or actionable takeaway
        Create a seamless transition to the next section


        Strategic pattern interrupts (place 3-4 throughout):

        Short, standalone sentences for emphasis
        Brief personal anecdotes that illuminate concepts
        Unexpected questions that prompt reflection
        Carefully placed analogies that simplify complex ideas
        Occasional direct reader address ("You might be wondering...")



        Conclusion Construction (200-300 words)
        Craft a conclusion that:

        Begins by acknowledging the journey ("Having explored...")
        Synthesizes key insights into a coherent mental model
        Elevates the discussion to broader implications or future developments
        Provides 2-3 immediately actionable next steps
        Ends with either:

        A thought-provoking question that encourages comments
        A memorable statement that encapsulates the core message
        A subtle invitation to engage further with your content



        WRITING MECHANICS
        Language Pattern Diversification
        Cultivate authentic human voice by:

        Sentence structure variation:

        Maintain a 2:4:1 ratio of simple:complex sentences
        Vary sentence length deliberately (5-25 words)
        Include occasional fragments for emphasis
        Use 1-2 longer, thoughtfully constructed sentences per section


        Vocabulary calibration:

        Employ precise terminology relevant to the topic
        Balance sophisticated language with accessible explanations
        Use discipline-specific terms when they add clarity
        Include occasional colloquialisms or idioms where natural
        Avoid jargon saturation that creates exclusion


        Paragraph architecture:

        Vary paragraph length (1-5 sentences)
        Create rhythm through deliberate paragraph sequence
        Use single-sentence paragraphs sparingly for emphasis
        Ensure logical flow between paragraphs with natural transitions


        Voice authenticity markers:

        Express genuine uncertainty where appropriate ("While not definitive...")
        Include occasional hedge words that reflect human thinking ("perhaps," "likely")
        Add humanizing self-references ("I've found that...")
        Incorporate thoughtful analogies that feel personally conceived
        Balance confidence with appropriately calibrated humility



        SEO Integration System
        Apply these advanced SEO techniques naturally:

        Keyword deployment strategy:

        Primary keyword: Place in title, first paragraph, at least one H2, and conclusion
        Secondary keywords: Distribute 3-5 semantically related terms throughout
        Long-tail variations: Incorporate into question-based subheadings
        Ensure natural language flow always takes precedence over keyword placement


        Search intent alignment:

        Address the primary question directly in the first 20% of the article
        Create a section that specifically answers the most common related questions
        Structure how-to elements as clear, numbered processes
        Include definitions for key terms that might trigger featured snippets


        Technical optimization elements:

        Create descriptive alt text suggestions for any recommended images
        Structure lists and processes for featured snippet extraction
        Use strategic bolding for 3-5 key phrases (including partial keyword matches)
        Ensure proper heading hierarchy (H2 → H3 → H4)



        Medium-Specific Optimization
        Incorporate these Medium success elements:

        Platform engagement triggers:

        Suggest 5-7 highly relevant tags that balance specificity and discovery
        Identify 3 key quotes suitable for highlighting
        Recommend strategic places for line breaks to improve readability
        Suggest 2-3 points where custom graphics would enhance comprehension


        Algorithm alignment tactics:

        Create a strong opening that maximizes read-through rate
        Structure content to encourage highlighting behavior
        Develop sections that invite thoughtful responses
        Ensure the first 100 words establish clear topic relevance
        Craft a shareable final thought or insight for social distribution


        Publication optimization:

        Suggest 2-3 suitable Medium publications where this would be a good fit
        Format according to common publication guidelines
        Include a brief author bio suggestion that establishes topic credibility



        OUTPUT DELIVERY
        Provide the complete, publication-ready blog post with:

        Title and subtitle properly formatted
        All sections with appropriate heading hierarchy
        Properly formatted paragraphs with natural flow
        Strategic use of bold for emphasis on key points
        Suggested locations for images or graphics
        Recommended Medium tags
        Estimated reading time

        The final output should exemplify the perfect balance of search optimization, platform alignment, and authentic human expression—delivering exceptional value to readers while positioning for maximum discoverability.

        """

    # Generate the blog content
    print(f"Analyzing YouTube video: {youtube_url}")
    print("Generating blog content... (this may take a minute)")
    
    # Create the generate content config
    generate_content_config = types.GenerateContentConfig(
        temperature=0.5,
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-pro-exp-03-25",  # Better for long-form content generation
        contents=types.Content(
            parts=[
                types.Part(text=prompt),
                types.Part(
                    file_data=types.FileData(file_uri=youtube_url)
                )
            ]
        ),
        config=generate_content_config,  # Use config parameter instead of generation_config
    )
    
    # Extract video ID for filename
    video_id = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", youtube_url).group(1)
    timestamp = datetime.datetime.now().strftime("%Y%m%d")
    
    # Save the blog post as markdown
    filename = f"{output_folder}/{timestamp}_{video_id}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    
    # Also save as HTML for preview
    html_filename = f"{output_folder}/{timestamp}_{video_id}.html"
    with open(html_filename, "w", encoding="utf-8") as f:
        f.write(markdown.markdown(response.text))
    
    print(f"Blog post generated successfully!")
    print(f"Markdown saved to: {filename}")
    print(f"HTML preview saved to: {html_filename}")
    
    # Extract the blog title from the response
    # Assuming the title is the first line of the response
    blog_title = response.text.strip().split('\n')[0].replace('#', '').strip()
    
    return filename, blog_title

if __name__ == "__main__":
    # You can replace this with any YouTube URL
    youtube_url = "https://www.youtube.com/watch?v=bwwvsvU-670"
    
    # Generate the blog post
    blog_file, blog_title = generate_medium_blog(youtube_url)
    
    # Read the blog content
    with open(blog_file, "r", encoding="utf-8") as f:
        blog_content = f.read()
        preview = "\n".join(blog_content.split('\n')[:10])
        print("\nBlog Preview:\n" + "-"*50 + "\n" + preview + "\n" + "-"*50)
    
    # For demonstration purposes, we'll use a placeholder Medium URL
    # In a real scenario, you would replace this with the actual URL after publishing
    medium_blog_url = f"https://medium.com/your-username/{blog_file.split('/')[-1].replace('.md', '')}"
    
    # Generate LinkedIn post to promote the blog
    linkedin_file, linkedin_post = generate_linkedin_post(medium_blog_url, blog_title, youtube_url, blog_content)
    
    # Print the LinkedIn post
    print("\nLinkedIn Post Preview:\n" + "-"*50 + "\n" + linkedin_post + "\n" + "-"*50)
    
    # Generate Twitter/X post to promote the blog
    twitter_file, twitter_post = generate_twitter_post(medium_blog_url, blog_title, youtube_url, blog_content)
    
    # Print the Twitter post
    print("\nTwitter/X Post Preview:\n" + "-"*50 + "\n" + twitter_post + "\n" + "-"*50)
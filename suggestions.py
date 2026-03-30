def get_skill_suggestions(missing_skills):
    suggestions_map = {
        "python": "Improve your Python skills by building real-world projects and practicing problem-solving regularly.",
        "machine learning": "Strengthen your machine learning skills by working on models and understanding algorithms deeply.",
        "pandas": "Enhance your data analysis skills by practicing data cleaning and manipulation using Pandas.",
        "sql": "Improve your SQL skills by writing advanced queries and working with real datasets.",
        "spark": "Learn Apache Spark to handle large-scale data processing and distributed computing.",
        "kafka": "Understand Kafka for real-time data streaming and event-driven architectures.",
        "testing": "Develop software testing skills by learning unit testing and automation frameworks like pytest.",
        "security": "Improve cybersecurity knowledge by learning secure coding practices and vulnerability assessment.",
        "penetration": "Gain penetration testing skills by practicing ethical hacking and using tools like Metasploit.",
        "network": "Strengthen networking fundamentals by understanding protocols, architectures, and troubleshooting techniques.",
        "communication": "Enhance communication skills by clearly explaining ideas and participating in team discussions.",
        "teamwork": "Improve teamwork by collaborating on group projects and contributing effectively.",
    }

    # 🔥 Different fallback templates (to avoid repetition)
    fallback_templates = [
        "Work on improving your {} skills through hands-on projects and continuous learning.",
        "Strengthen your {} skills by taking online courses and practicing regularly.",
        "Enhance your {} knowledge by applying it in real-world scenarios.",
        "Build expertise in {} by working on practical implementations and projects.",
    ]

    suggestions = []
    used = set()

    for i, skill in enumerate(missing_skills):
        skill_lower = skill.lower()

        if skill_lower in suggestions_map:
            suggestion = suggestions_map[skill_lower]
        else:
            template = fallback_templates[i % len(fallback_templates)]
            suggestion = template.format(skill)

        # 🔥 Avoid duplicates
        if suggestion not in used:
            suggestions.append(suggestion)
            used.add(suggestion)

    return suggestions
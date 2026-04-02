class AppraisalContextMixin:
    section_title = "Performance appraisals"

    def get_section_context(self) -> dict[str, str]:
        return {"section_title": self.section_title}

class SkillWorkflowReuserClient:
    LIBRARY = {
        "sales_proposal": [
            "Step 1: Research {company_name} background",
            "Step 2: Draft value proposition for {industry}",
            "Step 3: Prepare ROI estimate with {budget} in mind",
            "Step 4: Send proposal to {contact_email}"
        ],
        "weekly_report": [
            "Step 1: Pull metrics for the past 7 days",
            "Step 2: Write summary for {team_name}",
            "Step 3: Highlight blockers and {priority} items",
            "Step 4: Distribute report by {send_time}"
        ]
    }

    def run_workflow(self, workflow_name: str, input_variables: dict) -> dict:
        template = self.LIBRARY.get(workflow_name)
        if not template:
            return {"rendered_workflow": [], "workflow_found": False}
        rendered = [step.format(**input_variables) for step in template]
        return {"rendered_workflow": rendered, "workflow_found": True}

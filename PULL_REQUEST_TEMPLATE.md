# OrthoFi Change Form  
*This form is only required when merging to the main branch and/or production environment*  
*No sections are optional, they are required for PCI and SOC2 compliance*
*For auto-generated 'risk -> main' PRs, you can use the three dots menu in the top right of this comment to "Edit" and fill out the form*

---
### Description
> Provide a description of the background, problem, and solution.


### Potential Impact
- *Major → Affects security controls, authentication/authorization, encryption, networking rules, production infrastructure, or anything that could affect systems in the Cardholder Data Environment (CDE).*  
- *Medium → Affects production behavior or operations (e.g., performance, availability, user-facing features) but does not alter PCI-related security controls.*  
- *Minor → Only cosmetic, documentation-only, or limited to non-sensitive configs with no security or operational risk.*  

> Select one
- [ ] Major
- [ ] Medium
- [ ] Minor

### Compliance Checklist
> Assert that the following requirements have been met by checking the boxes.
- [ ] Change validated in a lower environment  
- [ ] No hardcoded credentials or secrets  
- [ ] No reduction in security controls  
- [ ] Changes follow principle of least privilege  
- [ ] Maintains network segmentation boundaries  
- [ ] Logging preserved for security events  
- [ ] Change implementor != change approver  

### Testing
> 1. Provide a description of how this change was validated in a lower environment.  
> 2. How will this be validated in production? *(optional if the same as lower environment)*  


### Rollback Plan
> How will this change be rolled back if needed?


---
*Implementation date and time will be recorded automatically via GitHub merge history*  
*Approval will be recorded automatically via GitHub PR approval by a PCI-designated approver*

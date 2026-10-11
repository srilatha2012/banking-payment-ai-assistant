import streamlit as st

from assistant_service import get_answer, get_wire_answer
from references import references, wire_references, wire_source


st.set_page_config(
    page_title="Banking Payment Operations Assistant",
    page_icon="🏦",
)

st.title("Banking Payment Operations Assistant")
st.write("Look up an ACH return code or explore a Wire topic.")

st.caption(
    "Educational reference tool. AI-generated explanations may be "
    "incomplete or incorrect; verify guidance against official "
    "documentation. This app does not verify real transactions. "
    "Do not enter account numbers, personal information, or "
    "confidential banking data."
)

payment_type = st.selectbox("Payment type", ["ACH", "Wire"])

if payment_type == "ACH":
    st.caption(
        f"Currently, the reference data covers {', '.join(references)}."
    )

    with st.form("ach_form"):
        return_code = st.text_input(
            "ACH return code",
            placeholder="Example: R01",
            max_chars=20,
        )
        submitted = st.form_submit_button("Explain code")

    if submitted:
        if not return_code.strip():
            st.warning("Please enter an ACH return code.")
        else:
            with st.spinner("Preparing answer..."):
                answer = get_answer(return_code)

            st.markdown(answer)

            reference = references.get(return_code.strip().upper())

            if reference is not None:
                with st.expander("View reference used"):
                    st.write(reference)
                    st.markdown(
                        "**Source:** "
                        "[Northern Trust — ACH Return Code Reference]"
                        "(https://web-xp2i-pws.ntrs.com/online_support/"
                        "inforpt/ach_return_codes.htm)"
                    )
                    st.caption(
                        "The stored definition is adapted from this source. "
                        "The app uses local reference text; it does not "
                        "retrieve the website during a request."
                    )

else:
    st.caption(
        "Currently supports one topic: international wire delays."
    )

    with st.form("wire_form"):
        topic = st.selectbox(
            "Wire topic",
            options=list(wire_references),
        )
        submitted = st.form_submit_button("Explain topic")

    if submitted:
        with st.spinner("Preparing answer..."):
            answer = get_wire_answer(topic)

        st.markdown(answer)

        with st.expander("View reference used"):
            st.write(wire_references[topic])
            st.markdown(
                f"**Source:** [{wire_source['title']}]"
                f"({wire_source['url']})"
            )
            st.caption(
                "This summary is adapted from Bank of America's "
                "international wire guidance. The app uses local "
                "reference text; it does not retrieve the website "
                "during a request."
            )
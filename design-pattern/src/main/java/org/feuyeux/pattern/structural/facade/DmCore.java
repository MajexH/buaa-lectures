package org.feuyeux.pattern.structural.facade;

public class DmCore {
    public static final String UNKNOWN = "unknown";
    private final NluCore nluCore;
    private final QasCore qasCore;
    private final FnCore fnCore;

    public DmCore(NluCore nluCore, QasCore qasCore, FnCore fnCore) {
        this.nluCore = nluCore;
        this.qasCore = qasCore;
        this.fnCore = fnCore;
    }

    public String dialog(String query) {
        String nlu = nluCore.q(query);
        if (UNKNOWN.equals(nlu)) {
            String qa = qasCore.q(query);
            return fnCore.fn(qa);
        } else {
            return fnCore.fn(nlu);
        }
    }
}
